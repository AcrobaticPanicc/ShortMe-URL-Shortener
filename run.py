# ------- standard library imports -------
import os

# ------- local imports -------
from app.app import app

production = os.environ.get("PRODUCTION", False)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run(host='127.0.0.1', port=8888, debug=True)
