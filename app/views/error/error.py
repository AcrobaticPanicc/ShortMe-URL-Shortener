# ------- 3rd party imports -------
from flask import Blueprint, render_template

error_blueprint = Blueprint('error_blueprint', __name__, template_folder='templates')


@error_blueprint.route('/error')
def error():
    return render_template('error.html')
