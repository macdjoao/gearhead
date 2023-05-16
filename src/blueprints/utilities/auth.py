from flask import jsonify
from src.blueprints.models.user_model import UserModel
from flask_jwt_extended import create_access_token


class Auth():
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def verify_email(self):
        user = UserModel.query.filter_by(email=self.email).first()
        if user:
            return True
        return False

    def generate_token(self):
        user = UserModel.query.filter_by(email=self.email).first()
        if self.verify_email() and user.verify_password(self.password):
            access_token = create_access_token(identity=self.email)
            return jsonify(access_token=access_token)
        else:
            return 'Incorrect email or password.'
