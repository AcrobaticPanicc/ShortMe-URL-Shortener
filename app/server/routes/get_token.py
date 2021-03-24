# ------- 3rd party imports -------
from flask import Blueprint, render_template

get_token_blueprint = Blueprint('get_token_blueprint', __name__, template_folder='templates')


@get_token_blueprint.route('/get_token')
def get_token():
    return render_template('get_token.html')
