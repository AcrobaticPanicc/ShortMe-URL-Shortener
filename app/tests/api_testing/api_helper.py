import json
from app import app as a


class ApiHelper:
    HEADERS = {
        'Authorization': f'Bearer {a.app.secret_key}'
    }
    print(HEADERS)

    def get_auth_token(self, app):
        r = app.test_client().get(
            '/api/get_token', headers=self.HEADERS
        )

        key = json.loads(r.get_data(as_text=True))
        return key
