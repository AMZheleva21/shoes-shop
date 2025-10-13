import os
from abc import ABC,abstractmethod
from flask import current_app, session
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    profile_image = db.Column(db.String(255), nullable=True)
    image_status = db.Column(db.String(50), default="pending")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class UserRole(ABC):
    @abstractmethod
    def get_role_description(self):
        pass

class AdminRole(UserRole):
    def get_role_description(self):
        return "Администратор с пълни права"

class CustomerRole(UserRole):
    def get_role_description(self):
        return "Клиент с права за пазаруване"

def display_role_info(role):
    print(role.get_role_description())

def is_admin():
    return session.get("is_admin", False)


def register_user(email, password):
    if User.query.filter_by(email=email).first():
        return False
    new_user = User(email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return True


def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        session["email"] = user.email
        session["is_admin"] = user.is_admin
        return user
    return None


def create_default_admin():
    admin = User.query.filter_by(email="admin@example.com").first()
    if not admin:
        admin = User(email="admin@example.com", is_admin=True)
        admin.set_password("admin123")
        db.session.add(admin)
        db.session.commit()
        print("Създаден е администратор: admin@example.com / admin123")


def change_email(user_id, new_email):
    user = User.query.get(user_id)
    if not user:
        return False, "Потребителят не съществува"
    if User.query.filter_by(email=new_email).first():
        return False, "Този имейл вече е зает"
    user.email = new_email
    db.session.commit()
    return True, "Имейлът е обновен"


def upload_profile_image(user_id, file):
    user = User.query.get(user_id)
    if not user or not file or not allowed_file(file.filename):
        return False, "Няма файл или форматът не е разрешен."

    filename = secure_filename(file.filename)
    upload_dir = os.path.join(current_app.root_path, "static/uploads/profile_images")
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, filename)
    file.save(file_path)

    user.profile_image = f"/static/uploads/profile_images/{filename}"
    user.image_status = "pending"
    db.session.commit()
    return True, "Снимката е качена и очаква одобрение от админ"


def update_profile(user_id, email=None, password=None, profile_image=None):
    user = User.query.get(user_id)
    if not user:
        return False, "Потребителят не съществува."

    if email and email != user.email:
        if User.query.filter_by(email=email).first():
            return False, "Имейлът вече е зает."
        user.email = email

    if password:
        user.set_password(password)

    if profile_image:
        success, msg = upload_profile_image(user_id, profile_image)
        if not success:
            return False, msg

    db.session.commit()
    return True, "Профилът е актуализиран успешно."
