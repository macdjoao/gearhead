from flask import Blueprint, jsonify, request
from src.blueprints.utilities.auth import Auth

login = Blueprint('login', __name__, url_prefix='/api/v1')


@login.route('/login', methods=['POST'])
def authenticate():
    try:
        email = (request.json.get('email')).lower()
        password = request.json.get('password')
        auth = Auth(email, password)
        return auth.generate_token()
    except Exception as exc:
        print(f'login Error: {exc}')
        return 'Login Failed'
