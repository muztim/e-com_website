from flask import Blueprint, render_template

products_bp = Blueprint('products_bp', __name__, template_folder='templates',
                        static_folder='static', static_url_path='assets')


@products_bp.route('/')
def product_list():
    return render_template('/products/view.html')


@products_bp.route('/view/<int:product_id>')
def product_view(product_id):
    #product = Product.query.get(product_id)
    return render_template('/products/view.html')
