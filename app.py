from flask import Flask
from auth.auth import auth_bp
from cart.cart import cart_bp
from general.general import general_bp
from api.api import api_bp
from products.products import products_bp

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix='/login')
app.register_blueprint(cart_bp, url_prefix='/cart')
app.register_blueprint(general_bp, url_prefix='')
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(products_bp, url_prefix='/products')


if __name__ == '__main__':
    app.run(debug=True)


