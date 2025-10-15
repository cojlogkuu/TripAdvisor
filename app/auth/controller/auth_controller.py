from flask import jsonify, request
from app.auth.service.auth_service import AuthService

class AuthController:
    @staticmethod
    def register():
        """
        Register a new user
        ---
        tags:
          - Authentication
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                  example: "John Doe"
                email:
                  type: string
                  example: "john@example.com"
                phone:
                  type: string
                  example: "+1234567890"
                password:
                  type: string
                  example: "securepassword123"
            example:
              name: "John Doe"
              email: "john@example.com"
              phone: "+1234567890"
              password: "securepassword123"
        responses:
          201:
            description: User registered successfully
            schema:
              type: object
            examples:
              application/json:
                message: "User registered successfully"
                customer_id: 1
          400:
            description: Invalid input or user already exists
            examples:
              application/json:
                message: "Email, name, and password are required"
        """
        data = request.json

        email = data.get('email')
        name = data.get('name')
        password = data.get('password')
        phone = data.get('phone')

        if not email or not name or not password:
            return jsonify({'message': 'Email, name, and password are required'}), 400

        result = AuthService.register_user(name, email, phone, password)

        if result.get('success'):
            return jsonify({
                'message': 'User registered successfully',
                'customer_id': result.get('customer_id')
            }), 201
        else:
            return jsonify({'message': result.get('message')}), 400

    @staticmethod
    def login():
        """
        Login with email and password
        ---
        tags:
          - Authentication
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                email:
                  type: string
                  example: "john@example.com"
                password:
                  type: string
                  example: "securepassword123"
            example:
              email: "john@example.com"
              password: "securepassword123"
        responses:
          200:
            description: Login successful
            schema:
              type: object
            examples:
              application/json:
                message: "Login successful"
                access_token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
                customer:
                  id: 1
                  name: "John Doe"
                  email: "john@example.com"
          401:
            description: Invalid credentials
            examples:
              application/json:
                message: "Invalid email or password"
          400:
            description: Missing required fields
            examples:
              application/json:
                message: "Email and password are required"
        """
        data = request.json

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'message': 'Email and password are required'}), 400

        result = AuthService.login_user(email, password)

        if result.get('success'):
            return jsonify({
                'message': 'Login successful',
                'access_token': result.get('access_token'),
                'customer': result.get('customer')
            }), 200
        else:
            return jsonify({'message': result.get('message')}), 401
