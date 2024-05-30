# Flask-Session issue

See: https://github.com/pallets-eco/flask-session/issues/251

To reproduce:

1. `python3 -m venv .venv`
1. `source .venv/bin/activate`
1. `pip install -e .`
1. `flask --app flask_session_issue run`
1. Hit http://127.0.0.1:5000/ until error logged
