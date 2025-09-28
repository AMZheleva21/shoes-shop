from flask import Flask

from controllers.admin_controller import admin_bp
from controllers.auth_controller import auth_bp
from controllers.catalog_controller import catalog_bp
from controllers.cart_controller import cart_bp

app = Flask(__name__)
app.secret_key = "supersecret"
app.register_blueprint(auth_bp)
app.register_blueprint(catalog_bp, url_prefix="/catalog")
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(cart_bp, url_prefix="/cart")




if __name__ == "__main__":
    app.run(debug=True)
