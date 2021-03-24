# ------- 3rd party imports -------
from flask import Blueprint, redirect, url_for

# ------- local imports -------
from app.server.db.models import Url
from app.server.db.extensions import db

redirect_to_url_blueprint = Blueprint('redirect_to_url_blueprint', __name__)


@redirect_to_url_blueprint.route('/<short_url>')
def redirect_to_url(short_url):
    """
    This function will query the database with the short_url and will
    redirect to the original url if it exist in the database.
    """
    url = Url.query.filter_by(short_url=short_url).first()

    if url:
        url.visits = url.visits + 1
        db.session.commit()
        return redirect(url.original_url)

    return redirect(url_for('page_not_found_blueprint.page_not_found'))
