# ------- standard library imports -------
import os

# ------- 3rd party imports -------
from flask import Blueprint, send_from_directory

app_blueprint = Blueprint('app_blueprint', __name__)


@app_blueprint.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app_blueprint.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
