from flask import Blueprint, render_template

general_bp = Blueprint('general_bp', __name__, template_folder='templates',
                       static_folder='static',
                       static_url_path='assets')


@general_bp.route('/')
def home():

    return render_template('general/index.html')






