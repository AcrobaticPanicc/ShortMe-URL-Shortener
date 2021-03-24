# ------- standard library imports -------
import json
import unittest

# ------- local imports -------
from time import sleep

from app.server.db.extensions import db
from app.server.db.models import Url
from app.app import create_app
from app.tests.api_testing.api_helper import ApiHelper


class TestApp(unittest.TestCase):
    VALID_URL = 'youtube.com'
    INVALID_URL = 'www.youtube.com/what?a=b&c=d'
    INVALID_PARAM = 'INVALID'

    def setUp(self):
        self.helper = ApiHelper()
        self.app = create_app(config_file='settings.py')
        sleep(1)
        self.key = self.helper.get_auth_token(self.app)

    def test_01_shorten_url_success(self):
        response = self.app.test_client().post(
            '/api/shorten',
            headers={'Authorization': f'Bearer {self.key}'},
            data={'url': self.VALID_URL}
        )

        res_dict = json.loads(response.get_data(as_text=True))

        short_url = res_dict['short_url']
        original_url = res_dict['original_url']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(short_url), 5)
        self.assertEqual(original_url, 'http://youtube.com')

    def test_02_shorten_url_fail(self):
        response = self.app.test_client().post(
            '/api/shorten',
            headers={'Authorization': f'Bearer {self.key}'},
            data={'url': self.INVALID_URL},
        )

        res_dict = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(res_dict['success'], False)
        self.assertEqual(res_dict['message'], 'could not shorten this URL (page_not_found)')

    def test_03_total_clicks(self):
        # add url to db
        response = self.app.test_client().post(
            '/api/shorten',
            headers={'Authorization': f'Bearer {self.key}'},
            data={'url': 'youtube.com'},
        )

        with self.app.app_context():
            url = Url.query.filter_by(original_url='http://youtube.com').first()
            short_url = url.short_url

        response = self.app.test_client().get(
            '/api/total_clicks',
            data={'url': short_url},
        )

        res_dict = json.loads(response.get_data(as_text=True))
        self.assertEqual(res_dict['total'], 0)

    def tearDown(self):
        db.session.remove()
        with self.app.app_context():
            db.drop_all()


if __name__ == '__main__':
    unittest.main()
