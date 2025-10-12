from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services.auth_service import login_user, register_user, User, update_profile
auth_bp = Blueprint("auth", __name__)
@auth_bp.route("/")
def index():
    return render_template("index.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if register_user(email, password):
            flash("Регистрацията е успешна! Влезте в профила си.", "success")
            return redirect(url_for("auth.login"))
        else:
            flash("Имейлът вече съществува!", "danger")
    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = login_user(email, password)
        if user:
            flash(f"Добре дошли, {user.email}!", "success")
            return redirect(url_for("catalog.catalog"))
        else:
            flash("Грешен имейл или парола.", "danger")
    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Излязохте от системата.", "info")
    return redirect(url_for("auth.login"))


@auth_bp.route("/profile", methods=["GET", "POST"])
def profile():
    email = session.get("email")
    if not email:
        flash("Моля, влезте, за да достъпите профила.", "danger")
        return redirect(url_for("auth.login"))

    user = User.query.filter_by(email=email).first()
    if not user:
        flash("Потребителят не съществува.", "danger")
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        new_email = request.form.get("email")
        new_password = request.form.get("password")
        profile_image = request.files.get("profile_image")

        success, msg = update_profile(user.id, email=new_email, password=new_password, profile_image=profile_image)
        flash(msg, "success" if success else "danger")
        if success and new_email:
            session["email"] = new_email

        return redirect(url_for("auth.profile"))

    return render_template("profile.html", user=user)
