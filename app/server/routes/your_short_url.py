# ------- 3rd party imports -------
import flask
from flask import Blueprint, render_template, request

your_short_url_blueprint = Blueprint('your_short_url_blueprint', __name__, template_folder='templates')


@your_short_url_blueprint.route('/your_short_url')
def your_short_url():
    original_url = request.args['original_url']
    short_url = request.args['short_url']
    base_url = flask.url_for("index_blueprint.index", _external=True)
    full_short_url = f'{base_url}{short_url}'
    full_short_url = full_short_url.replace('http://www.', '')

    return render_template('your_short_url.html',
                           original_url=original_url,
                           short_url=short_url,
                           full_short_url=full_short_url)
