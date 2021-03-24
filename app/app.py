from app.setup.setup import create_app

CONFIG_FILE = 'settings.py'

app = create_app(config_file=CONFIG_FILE)
