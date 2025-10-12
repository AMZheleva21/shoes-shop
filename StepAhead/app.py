from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from controllers.auth_controller import auth_bp
from controllers.catalog_controller import catalog_bp
from controllers.admin_controller import admin_bp
from controllers.cart_controller import cart_bp


app.register_blueprint(auth_bp)
app.register_blueprint(catalog_bp, url_prefix="/catalog")
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(cart_bp, url_prefix="/cart")

from services import auth_service, catalog_service

with app.app_context():
    db.create_all()
    auth_service.create_default_admin()
    catalog_service.seed_products()

if __name__ == "__main__":
    app.run(debug=True)
