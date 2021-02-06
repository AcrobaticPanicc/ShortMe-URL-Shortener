# ------- 3rd party imports -------
from flask import render_template, Blueprint

index_blueprint = Blueprint('index_blueprint', __name__, template_folder='templates')


@index_blueprint.route("/")
def index():
    return render_template('index.html')
