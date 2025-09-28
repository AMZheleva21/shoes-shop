from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from services import cart_service, order_service

cart_bp = Blueprint("cart", __name__)

@cart_bp.route("/")
def view_cart():
    if "email" not in session:
        flash("Трябва да влезете, за да видите кошницата.")
        return redirect(url_for("auth.login"))

    user_email = session["email"]
    cart = cart_service.get_cart(user_email)
    total = cart_service.get_cart_total(user_email)
    return render_template("cart.html", cart=cart, total=total)

@cart_bp.route("/add/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    if "email" not in session:
        flash("Трябва да влезете, за да добавяте в кошницата.")
        return redirect(url_for("auth.login"))

    user_email = session["email"]
    quantity = int(request.form.get("quantity", 1))

    if cart_service.add_to_cart(user_email, product_id, quantity):
        flash("Продуктът е добавен в кошницата.")
    else:
        flash("Недостатъчна наличност.")

    return redirect(url_for("catalog.catalog"))

@cart_bp.route("/remove/<int:product_id>")
def remove_from_cart(product_id):
    if "email" not in session:
        return redirect(url_for("auth.login"))

    user_email = session["email"]
    cart_service.remove_from_cart(user_email, product_id)
    flash("Продуктът е премахнат от кошницата.")
    return redirect(url_for("cart.view_cart"))

@cart_bp.route("/checkout", methods=["GET", "POST"])
def checkout():
    if "email" not in session:
        return redirect(url_for("auth.login"))

    user_email = session["email"]

    if request.method == "POST":
        address = request.form["address"]
        payment = request.form["payment"]
        order = order_service.create_order(user_email, address, payment)
        if order:
            flash("Поръчката е успешно направена!")
            return redirect(url_for("catalog.catalog"))
        else:
            flash("Кошницата е празна.")
            return redirect(url_for("cart.view_cart"))

    return render_template("checkout.html")
