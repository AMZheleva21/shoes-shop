from flask import session

class User:
    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.__password = password
        self.is_admin = is_admin

    def check_password(self, password):
        return self.__password == password

    def __repr__(self):
        return f"<User {self.email}, admin={self.is_admin}>"


class Admin(User):
    def __init__(self, email, password):
        super().__init__(email, password, is_admin=True)


class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password, is_admin=False)


users = [
    Admin("admin@example.com", "admin123")
]

def is_admin():
    return session.get("is_admin", False)

def register_user(email, password):
    for user in users:
        if user.email == email:
            return False
    users.append(Customer(email, password))
    print(f"{email} е регистриран успешно!")
    return True


def login_user(email, password):
    for user in users:
        if user.email == email and user.check_password(password):
            session["email"] = user.email
            session["is_admin"] = user.is_admin
            return user
    return None


def get_all_users():
    return users
