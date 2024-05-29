from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite+pysqlite:///:memory:"
    app.config["SESSION_SQLALCHEMY"] = SQLAlchemy(app)
    app.config["SESSION_TYPE"] = "sqlalchemy"
    Session(app)

    @app.route("/")
    def home():
        if "foo" not in session:
            session["foo"] = "bar"

        return """
            <html>
                <head>
                    <link href="static/main1.css" rel="stylesheet"/>
                    <link href="static/main2.css" rel="stylesheet"/>
                    <link href="static/main3.css" rel="stylesheet"/>
                </head>
                <body>
                    <h1>Flask-Session issue</h1>
                </body>
            </html>
        """

    return app
