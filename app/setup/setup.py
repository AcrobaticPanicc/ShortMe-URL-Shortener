# ------- standard library imports -------
import os

# ------- 3rd party imports -------
from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv

# ------- local imports -------
from app.server.db.extensions import db
from app.server.db.models import AuthToken
from app.server.routes.index import index_blueprint
from app.server.routes.internal.redirect_to_url import redirect_to_url_blueprint
from app.server.routes.internal.favicon import app_blueprint
from app.server.routes.internal.send_verification_code import send_otp_blueprint
from app.server.routes.internal.shorten_url import shorten_url_blueprint
from app.server.routes.your_short_url import your_short_url_blueprint
from app.server.routes.total_clicks import total_clicks_blueprint
from app.server.routes.error import error_blueprint
from app.server.routes.page_not_found import page_not_found_blueprint
from app.server.routes.api_doc import api_doc_blueprint
from app.server.routes.get_token import get_token_blueprint
from app.server.routes.your_api_token import your_api_token_blueprint
from app.server.routes.verify_code import verify_code_blueprint

from app.server.api.api import Shorten, TotalClicks, GetToken


def create_app(config_file):
    """
    Creating and returning the app
    """
    app_path = os.path.dirname(os.path.abspath(__file__))
    project_folder = os.path.expanduser(app_path)
    load_dotenv(os.path.join(project_folder, '.env'))

    app = Flask(__name__, template_folder='../client/templates', static_folder='../client/static')
    api = Api(app)
    app.config.from_pyfile(config_file)

    db.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()

        app_auth_token = app.secret_key
        auth_token = AuthToken(auth_token=app_auth_token)
        db.session.add(auth_token)
        db.session.commit()

        api.add_resource(Shorten, '/api/shorten')
        api.add_resource(GetToken, '/api/get_token')
        api.add_resource(TotalClicks, '/api/total_clicks')

        app.register_blueprint(index_blueprint)
        app.register_blueprint(page_not_found_blueprint)
        app.register_blueprint(redirect_to_url_blueprint)
        app.register_blueprint(your_short_url_blueprint)
        app.register_blueprint(total_clicks_blueprint)
        app.register_blueprint(error_blueprint)
        app.register_blueprint(app_blueprint)
        app.register_blueprint(api_doc_blueprint)
        app.register_blueprint(get_token_blueprint)
        app.register_blueprint(send_otp_blueprint)
        app.register_blueprint(verify_code_blueprint)
        app.register_blueprint(your_api_token_blueprint)
        app.register_blueprint(shorten_url_blueprint)
        return app
