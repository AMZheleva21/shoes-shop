from flask import Blueprint, render_template, request
from services import cart_service, order_service
from flask import  session, redirect, url_for, send_file, flash
from io import BytesIO
from reportlab.pdfgen import canvas

cart_bp = Blueprint("cart", __name__)

@cart_bp.route("/")
def view_cart():
    if "email" not in session:
        flash("Трябва да влезете в профила си, за да видите кошницата.")
        return redirect(url_for("auth.login"))

    user_email = session["email"]
    cart = cart_service.get_cart(user_email)
    total = cart_service.get_cart_total(user_email)
    return render_template("cart.html", cart=cart, total=total)

@cart_bp.route("/add/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    if "email" not in session:
        flash("Трябва да влезете в профила си, за да добавите продукт в кошницата")
        return redirect(url_for("auth.login"))

    user_email = session["email"]
    quantity = int(request.form.get("quantity", 1))

    if cart_service.add_to_cart(user_email, product_id, quantity):
        flash("Продуктът е добавен в кощницата.")
    else:
        flash("Няма достатъчно количество.")
    return redirect(url_for("cart.view_cart"))

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
    order = None

    if request.method == "POST":
        address = request.form["address"]
        payment = request.form["payment"]
        order = order_service.create_order(user_email, address, payment)
        if order:
            flash("Поръчката е завършена успешно!")
        else:
            flash("Кошницата е празна!")

    return render_template("checkout.html", order=order)



@cart_bp.route("/order_pdf/<int:order_id>")
def order_pdf(order_id):
    if "email" not in session:
        flash("Трябва да влезете в профила си, за да видите поръчката.")
        return redirect(url_for("auth.login"))

    user_email = session["email"]

    order = order_service.get_order_with_items(order_id, user_email)
    if not order:
        flash("Поръчката не съществува.")
        return redirect(url_for("cart.view_cart"))

    buffer = BytesIO()
    c = canvas.Canvas(buffer)

    y = 800
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, f"Поръчка № {order['id']}")
    y -= 25
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Потребител: {user_email}")
    y -= 20
    c.drawString(50, y, f"Начин на плащане: {order['payment']}")
    y -= 25

    c.drawString(50, y, "Артикули:")
    y -= 20

    for item in order['items']:
        text = f"{item['name']} ({item.get('description', '')}) - {item['quantity']} бр. - {item['price']:.2f} лв"
        c.drawString(50, y, text)
        y -= 20

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Обща сума: {order['total']:.2f} лв")

    c.showPage()
    c.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"order_{order_id}.pdf",
        mimetype='application/pdf'
    )

