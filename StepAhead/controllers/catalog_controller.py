from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services import catalog_service
from services.auth_service import is_admin

catalog_bp = Blueprint("catalog", __name__)

@catalog_bp.route("/", methods=["GET", "POST"])
def catalog():
    if request.method == "POST":
        if not is_admin():
            flash("Нямате достъп до добавяне на продукти.")
            return redirect(url_for("catalog.catalog"))

        name = request.form["name"]
        description = request.form["description"]
        color = request.form["color"]
        sizes = [s.strip() for s in request.form["sizes"].split(",")]
        price = float(request.form["price"])
        stock = int(request.form["stock"])
        category = request.form["category"]
        subcategory = request.form["subcategory"]
        image_url = request.form.get("image_url")

        catalog_service.add_product(
            name, description, color, sizes, price, stock, category, subcategory, image_url
        )
        flash("Продуктът е добавен успешно.")
        return redirect(url_for("catalog.catalog"))

    query = request.args.get("q", "")
    min_price = request.args.get("min_price")
    max_price = request.args.get("max_price")
    size = request.args.get("size")
    in_stock = request.args.get("in_stock")
    category = request.args.get("category")
    subcategory = request.args.get("subcategory")
    sort_by = request.args.get("sort_by", "price")
    order = request.args.get("order", "asc")

    products = catalog_service.get_all_products()

    if query:
        products = catalog_service.search_products(query)
    elif any([min_price, max_price, size, in_stock, category, subcategory]):
        products = catalog_service.filter_products(
            min_price=float(min_price) if min_price else None,
            max_price=float(max_price) if max_price else None,
            size=int(size) if size else None,
            in_stock=True if in_stock else None,
            category=category if category else None,
            subcategory=subcategory if subcategory else None,
        )

    products = catalog_service.sort_products(products, by=sort_by, descending=(order == "desc"))

    return render_template(
        "catalog.html",
        products=products,
        is_admin=is_admin(),
        query=query,
        selected_category=category,
        selected_subcategory=subcategory,
        sort_by=sort_by,
        order=order,
        show_add_form=is_admin(),
    )

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
        sizes = [s.strip() for s in request.form["sizes"].split(",")]
        price = float(request.form["price"])
        stock = int(request.form["stock"])
        category = request.form["category"]
        subcategory = request.form["subcategory"]
        image_url = request.form.get("image_url")

        catalog_service.update_product(product_id, name, description, color, sizes, price, stock, category, subcategory, image_url)
        flash("Продуктът е редактиран успешно.")
        return redirect(url_for("catalog.catalog"))

    return render_template(
        "edit_product.html",
        product=product,
        is_admin=is_admin()
    )

@catalog_bp.route("/delete/<int:product_id>")
def delete_product(product_id):
    if not is_admin():
        flash("Нямате достъп до изтриване на продукти.")
        return redirect(url_for("catalog.catalog"))

    catalog_service.delete_product(product_id)
    flash("🗑Продуктът е изтрит успешно.")
    return redirect(url_for("catalog.catalog"))


@catalog_bp.route("/product/<int:product_id>", methods=["GET", "POST"])
def product_detail(product_id):
    product = catalog_service.get_product_by_id(product_id)
    if not product:
        flash("Продуктът не е намерен.")
        return redirect(url_for("catalog.catalog"))

    if request.method == "POST":
        if "email" not in session:
            flash(" Трябва да сте влезли, за да оставите коментар.")
            return redirect(url_for("auth.login"))

        rating = int(request.form["rating"])
        comment = request.form["comment"]
        catalog_service.add_review(product_id, session["email"], rating, comment)
        flash("Вашият отзив е добавен.")
        return redirect(url_for("catalog.product_detail", product_id=product_id))

    reviews = catalog_service.get_reviews_for_product(product_id)
    average_rating = catalog_service.get_average_rating(product_id)

    return render_template(
        "product_detail.html",
        product=product,
        reviews=reviews,
        average_rating=average_rating
    )