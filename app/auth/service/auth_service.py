import bcrypt
from app.auth.dao.customer_dao import CustomerDAO
from app.auth.dao.security_dao import SecurityDAO
from app.auth.utils.jwt_utils import create_access_token

class AuthService:
    @staticmethod
    def register_user(name, email, phone, password):
        """Register a new user with hashed password"""
        try:
            # Check if user already exists
            existing_customer = CustomerDAO.get_customer_by_email(email)
            if existing_customer:
                return {'success': False, 'message': 'User with this email already exists'}

            # Create customer
            customer_data = {
                'name': name,
                'email': email,
                'phone': phone
            }
            customer = CustomerDAO.create_customer(customer_data)

            if not customer:
                return {'success': False, 'message': 'Failed to create customer'}

            # Hash password
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # Create security entry
            security_data = {
                'customer_id': customer.id,
                'password': hashed_password.decode('utf-8')
            }
            SecurityDAO.create_security(security_data)

            return {
                'success': True,
                'customer_id': customer.id
            }

        except Exception as e:
            return {'success': False, 'message': f'Registration failed: {str(e)}'}

    @staticmethod
    def login_user(email, password):
        """Authenticate user and return JWT token"""
        try:
            # Get customer by email
            customer = CustomerDAO.get_customer_by_email(email)

            if not customer:
                return {'success': False, 'message': 'Invalid email or password'}

            # Get security record
            security = SecurityDAO.get_security_by_customer_id(customer.id)

            if not security:
                return {'success': False, 'message': 'Invalid email or password'}

            # Verify password
            if not bcrypt.checkpw(password.encode('utf-8'), security.password.encode('utf-8')):
                return {'success': False, 'message': 'Invalid email or password'}

            # Generate JWT token
            token_data = {
                'customer_id': customer.id,
                'email': customer.email,
                'name': customer.name
            }
            access_token = create_access_token(token_data)

            return {
                'success': True,
                'access_token': access_token,
                'customer': customer.to_dict()
            }

        except Exception as e:
            return {'success': False, 'message': f'Login failed: {str(e)}'}
