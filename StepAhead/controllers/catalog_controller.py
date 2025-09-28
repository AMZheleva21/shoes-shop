from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services import catalog_service
from services.auth_service import is_admin
catalog_bp = Blueprint("catalog", __name__)

@catalog_bp.route("/", methods=["GET", "POST"])
def catalog():
    query = request.args.get("q", "")
    min_price = request.args.get("min_price")
    max_price = request.args.get("max_price")
    size = request.args.get("size")
    in_stock = request.args.get("in_stock")

    products = catalog_service.get_all_products()

    if query:
        products = catalog_service.search_products(query)

    if min_price or max_price or size or in_stock:
        products = catalog_service.filter_products(
            min_price=float(min_price) if min_price else None,
            max_price=float(max_price) if max_price else None,
            size=int(size) if size else None,
            in_stock=True if in_stock else None,
        )

    return render_template("catalog.html", products=products, is_admin=is_admin(), query=query)

@catalog_bp.route("/add", methods=["GET", "POST"])
def add_product():
    if not is_admin():
        flash("Нямате достъп до добавяне на продукти.")
        return redirect(url_for("catalog.catalog"))

    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        color = request.form["color"]
        sizes = [int(s) for s in request.form["sizes"].split(",")]
        price = float(request.form["price"])
        stock = int(request.form["stock"])
        catalog_service.add_product(name, description, color, sizes, price, stock)
        flash("Продуктът е добавен успешно.")
        return redirect(url_for("catalog.catalog"))

    return render_template("catalog.html", products=catalog_service.get_all_products(), is_admin=True, show_add_form=True)

@catalog_bp.route("/edit/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    if not is_admin():
        flash("Нямате достъп до редактиране на продукти.")
        return redirect(url_for("catalog.catalog"))

    product = catalog_service.get_product_by_id(product_id)
    if not product:
        flash("Продуктът не е намерен.")
        return redirect(url_for("catalog.catalog"))

    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        color = request.form["color"]
        sizes = [int(s) for s in request.form["sizes"].split(",")]
        price = float(request.form["price"])
        stock = int(request.form["stock"])
        catalog_service.update_product(product_id, name, description, color, sizes, price, stock)
        flash("Продуктът е редактиран успешно.")
        return redirect(url_for("catalog.catalog"))

    return render_template("catalog.html", products=catalog_service.get_all_products(), is_admin=True, edit_product=product)

@catalog_bp.route("/delete/<int:product_id>")
def delete_product(product_id):
    if not is_admin():
        flash("Нямате достъп до изтриване на продукти.")
        return redirect(url_for("catalog.catalog"))

    catalog_service.delete_product(product_id)
    flash("Продуктът е изтрит успешно.")
    return redirect(url_for("catalog.catalog"))
