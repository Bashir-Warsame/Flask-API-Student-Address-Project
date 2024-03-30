from flask import Flask
from .database import db
from .serializer import ma
from .init_jwt import jwt
from .views.student import student_bp
from .views.address import address_bp
from .views.auth_user import auth_blueprint
from datetime import timedelta


def create_app():
    """Flask Factory"""

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin@localhost/flask_assessment"

    app.config["JWT_SECRET_KEY"] = "Apples321"
    app.config["JWT_COOKIE_SECURE"] = False
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    app.config["JWT_COOKIE_CSRF_PROTECT"] = False
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()
        db.session.commit()

    app.register_blueprint(student_bp)
    app.register_blueprint(address_bp)
    app.register_blueprint(auth_blueprint)

    return app
