# ------- standard library imports -------
import requests

# ------- 3rd party imports -------
from flask_restful import Resource, reqparse

# ------- local imports -------
from app.server.db.extensions import db
from app.server.api.api_auth import auth
from app.server.db.models import Url, AuthToken

shorten_parser = reqparse.RequestParser()
total_clicks_parser = reqparse.RequestParser()

shorten_parser.add_argument('url', type=str, help='URL parameter is missing', required=True)
total_clicks_parser.add_argument('url', type=str, help='Short URL is missing', required=True)


class Shorten(Resource):
    """
    Return a short URL from a given URL
    URL: /api/shorten
    METHOD: POST
    PARAMS: url: long URL
    HEADERS: Authorization: (Bearer <key>)
    RETURN: dictionary with the short URL
    """

    decorators = [auth.login_required]

    @staticmethod
    def post():
        args = shorten_parser.parse_args()
        url = args['url']
        original_url = url if url.startswith('http') else ('http://' + url)

        try:
            res = requests.get(original_url)

            if res.status_code == 200:
                url = Url(original_url=original_url)

                db.session.add(url)
                db.session.commit()

                return dict(
                    short_url=url.short_url,
                    original_url=url.original_url,
                    success=True
                ), 200

            else:
                """in case of page_not_found response from the URL given"""
                return dict(
                    success=False,
                    message='could not shorten this URL (page_not_found)'
                ), 404

        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
            return dict(
                success=False,
                message='could not shorten this URL (page_not_found)'
            ), 404


class TotalClicks(Resource):
    """
    return the total clicks of a short URL
    URL: /api/total_clicks
    METHOD: GET
    PARAMS: short url
    RETURN: dictionary with the total short url visits.
    """

    @staticmethod
    def get():
        args = total_clicks_parser.parse_args()
        url = args['url'].split('/')[-1]

        try:
            url = Url.query.filter_by(short_url=url).first()

            return dict(
                total=url.visits,
                short_url=url.short_url,
                original_url=url.original_url,
                success=True
            ), 200

        except AttributeError:
            return dict(
                success=False,
                message='could not find the URL (page_not_found)'
            ), 404


class GetToken(Resource):
    """
    Return a unique API authorization token. Used only internaly by the web app.
    URL: /api/get_token
    METHOD: GET
    RETURN: unique API authorization token
    AuthToken: Required
    """
    decorators = [auth.login_required]

    @staticmethod
    def get():
        token = AuthToken()
        db.session.add(token)
        db.session.commit()
        return str(token)
