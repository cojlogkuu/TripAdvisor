import jwt
import os
from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify

SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-secret-key-change-this')
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 300

def create_access_token(data: dict):
    """Generate a JWT access token"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: str):
    """Decode and validate a JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def token_required(f):
    """Decorator to protect routes with JWT authentication"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({'message': 'Token format invalid. Use: Bearer <token>'}), 401

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        payload = decode_token(token)
        if payload is None:
            return jsonify({'message': 'Token is invalid or expired'}), 401

        request.current_user = payload
        return f(*args, **kwargs)

    return decorated
