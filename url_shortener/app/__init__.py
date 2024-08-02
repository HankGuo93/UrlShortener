from flask import Flask
from controllers.url_controller import url_bp

from infrastructure.db.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE_URL']
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(url_bp)

    return app