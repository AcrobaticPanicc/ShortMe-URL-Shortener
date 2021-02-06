# ------- 3rd party imports -------
from flask import Blueprint, render_template, request, url_for

your_api_token_blueprint = Blueprint('your_api_token_blueprint', __name__, template_folder='templates')


@your_api_token_blueprint.route('/your_api_token')
def your_api_token():
    auth_token = request.args.get("auth_token")

    if auth_token:
        return render_template('your_api_token.html', auth_token=auth_token)

    else:
        return render_template(url_for('page_not_found_blueprint.page_not_found'))
