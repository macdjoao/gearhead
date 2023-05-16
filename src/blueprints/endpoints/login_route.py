from flask import Blueprint, jsonify, request
from src.blueprints.utilities.auth import Auth
from src.blueprints.models.user_model import UserModel
from werkzeug.security import generate_password_hash, check_password_hash

login = Blueprint('login', __name__, url_prefix='/api/v1')


@login.route('/login', methods=['POST'])
def authenticate():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        auth = Auth(email, password)
        return auth.generate_token()
    except Exception as exc:
        print(f'login Error: {exc}')
        return 'Login Failed'
