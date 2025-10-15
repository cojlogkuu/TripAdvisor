from flask import Blueprint
from app.auth.controller.auth_controller import AuthController

auth_bp = Blueprint('auth', __name__)

auth_bp.add_url_rule('/auth/register', 'register', AuthController.register, methods=['POST'])
auth_bp.add_url_rule('/auth/login', 'login', AuthController.login, methods=['POST'])
