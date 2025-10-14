from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from services import promo_service
from datetime import datetime
from services.auth_service import is_admin
promo_bp = Blueprint("promo", __name__, url_prefix="/promo")

@promo_bp.route("/")
def promo_calendar():
    return render_template("promo_calendar.html", is_admin=is_admin())

@promo_bp.route("/api")
def promo_api():
    promotions = promo_service.get_all_promotions()
    events = []
    for p in promotions:
        data = p.to_dict()

        events.append({
            "title": f"{data['category']} {data['subcategory']} - {data['title']} (-{data['discount']}%)",
            "start": data["start"],
            "end": data["end"],
            "description": (
                f"{data['description'] or 'Без описание'}\n\n"
                f"Категория: {data['category']} {data['subcategory']}\n"
                f"Отстъпка: {data['discount']}%\n"
                f"От: {datetime.strptime(data['start'], '%Y-%m-%d').strftime('%d.%m.%Y')} "
                f"до: {datetime.strptime(data['end'], '%Y-%m-%d').strftime('%d.%m.%Y')}"
            ),
            "backgroundColor": "#0d6efd",
            "borderColor": "#0d6efd"
        })
    return jsonify(events)

@promo_bp.route("/add", methods=["GET", "POST"])
def add_promo():
    if not is_admin():
        flash("Нямате достъп.")
        return redirect(url_for("catalog.catalog"))

    if request.method == "POST":
        try:
            title = request.form["title"]
            description = request.form.get("description")
            discount = int(request.form["discount"])
            start_date = datetime.strptime(request.form["start_date"], "%Y-%m-%d").date()
            end_date = datetime.strptime(request.form["end_date"], "%Y-%m-%d").date()
            category = request.form["category"]
            subcategory = request.form["subcategory"]

            promo_service.add_promotion(
                title=title,
                description=description,
                discount=discount,
                start_date=start_date,
                end_date=end_date,
                category=category,
                subcategory=subcategory
            )

            flash(f"Промоцията за {category} {subcategory} обувки е създадена успешно!", "success")
            return redirect(url_for("promo.promo_calendar"))

        except Exception as e:
            flash(f"Грешка при създаване на промоция: {e}", "error")

    return render_template("promo_form.html")