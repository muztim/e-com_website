from flask import Flask
from auth.auth import auth_bp
from cart.cart import cart_bp
from general.general import general_bp
from api.api import api_bp
from products.products import products_bp
from app_factory import db


app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix='/login')
app.register_blueprint(cart_bp, url_prefix='/cart')
app.register_blueprint(general_bp, url_prefix='')
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(products_bp, url_prefix='/products')


# create the extension
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)



if __name__ == '__main__':
    app.run(debug=True)


