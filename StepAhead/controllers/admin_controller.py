from flask import Blueprint, render_template, redirect, url_for, flash, request
from services import order_service
from services.auth_service import User, db

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/approve_images")
def approve_images():
    pending_users = User.query.filter_by(image_status="pending").all()
    return render_template("admin/approve_images.html", users=pending_users)


@admin_bp.route("/admin/approve_image/<int:user_id>")
def approve_image(user_id):
    user = User.query.get(user_id)
    if user:
        user.image_status = "approved"
        db.session.commit()
        flash(f"Снимката на {user.email} е одобрена.", "success")
    return redirect(url_for("admin.approve_images"))


@admin_bp.route("/admin/reject_image/<int:user_id>")
def reject_image(user_id):
    user = User.query.get(user_id)
    if user:
        user.image_status = "rejected"
        db.session.commit()
        flash(f"Снимката на {user.email} е отхвърлена.", "danger")
    return redirect(url_for("admin.approve_images"))


@admin_bp.route("/last_buyer", methods=["GET", "POST"])
def last_buyer():
    result = None
    if request.method == "POST":
        keyword = request.form.get("keyword")
        if keyword:
            result = order_service.get_last_buyer_by_product_name(keyword)
            if not result:
                flash(f"Няма намерени покупки на продукти, съдържащи '{keyword}' в името.")
    return render_template("admin_last_buyer.html", result=result)