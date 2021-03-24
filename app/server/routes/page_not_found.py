# ------- 3rd party imports -------
from flask import Blueprint, render_template

page_not_found_blueprint = Blueprint('page_not_found_blueprint', __name__, template_folder='templates')


@page_not_found_blueprint.route('/page_not_found')
def page_not_found():
    return render_template('404.html')
