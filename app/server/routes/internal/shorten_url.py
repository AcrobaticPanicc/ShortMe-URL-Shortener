# ------- standard library imports -------
import json
import requests

# ------- 3rd party imports -------
import flask
from flask import Blueprint, request, redirect, url_for

# ------- local imports -------
from app import app

shorten_url_blueprint = Blueprint('shorten_url_blueprint', __name__, template_folder='templates')


@shorten_url_blueprint.route('/shorten', methods=['POST'])
def shorten_url():
    base_url = flask.url_for("index_blueprint.index", _external=True)
    original_url = request.form['original_url']
    shorten_endpoint = base_url + 'api/shorten'

    params = {
        'url': original_url
    }

    headers = {
        'Authorization': f'Bearer {app.app.secret_key}'
    }

    response = requests.post(shorten_endpoint, headers=headers, params=params)

    if response.status_code == 200:
        response = json.loads(response.text)
        short_url = response['short_url']
        original_url = response['original_url']

        return redirect(url_for('your_short_url_blueprint.your_short_url',
                                short_url=short_url,
                                original_url=original_url))
    else:
        return redirect(url_for('error_blueprint.error'))
