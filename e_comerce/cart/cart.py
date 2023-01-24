from flask import Blueprint, render_template


cart_bp = Blueprint('cart_bp', __name__, template_folder='templates',
                    static_folder='static',
                    static_url_path='assets')


@cart_bp.route('/')
def cart_view():
    return render_template('/cart/view.html')


@cart_bp.route('/checkout')
def checkout():
    return render_template('/cart/checkout.html')





