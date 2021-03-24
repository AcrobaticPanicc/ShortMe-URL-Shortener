import json
from app.app import app as a


class ApiHelper:
    HEADERS = {
        'Authorization': f'Bearer {a.secret_key}'
    }

    def get_auth_token(self, app):
        r = app.test_client().get(
            '/api/get_token', headers=self.HEADERS
        )

        print(r.get_data(as_text=True))

        key = json.loads(r.get_data(as_text=True))
        return key
