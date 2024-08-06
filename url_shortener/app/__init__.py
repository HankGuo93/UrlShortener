from flask import Flask
from flask_restx import Api
from controllers.url_controller import url_ns

from infrastructure.db.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE_URL']
    db.init_app(app)
    migrate.init_app(app, db)

    api = Api(app, version='1.0', title='URL Shortener API', description='A simple URL shortener API', doc='/swagger')
    api.add_namespace(url_ns, path='/api')

    return app