from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services import auth_service
auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def index():
    return render_template("index.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if auth_service.register_user(email, password):
            flash("Регистрацията е успешна! Влезте в профила си.")
            return redirect(url_for("auth.login"))
        else:
            flash("Имейлът вече съществува!")

    return render_template("register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = auth_service.login_user(email, password)

        if user:
            session["email"] = user.email
            session["is_admin"] = user.is_admin
            return redirect(url_for("catalog.catalog"))
        else:
            flash("Грешен имейл или парола.")

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Излязохте от системата.")
    return redirect(url_for("auth.login"))
