from flask import Blueprint
from app.auth.controller.customer_controller import CustomerController

customer_bp = Blueprint('customer', __name__)

customer_bp.add_url_rule('/customers', 'get_all_customers', CustomerController.get_all_customers, methods=['GET'])
customer_bp.add_url_rule('/customers/favourites', 'get_customers_with_favorites', CustomerController.get_favorite_customer, methods=['GET'])
customer_bp.add_url_rule('/customers/<int:customer_id>', 'get_customer', CustomerController.get_customer, methods=['GET'])
customer_bp.add_url_rule('/customers', 'create_customer', CustomerController.create_customer, methods=['POST'])
customer_bp.add_url_rule('/customers/<int:customer_id>', 'update_customer', CustomerController.update_customer, methods=['PUT'])
customer_bp.add_url_rule('/customers/<int:customer_id>', 'delete_customer', CustomerController.delete_customer, methods=['DELETE'])
customer_bp.add_url_rule('/customers/favourites', 'set_customers_with_favorites', CustomerController.add_favourites_establishment, methods=['POST'])
customer_bp.add_url_rule('/customers/multiple', 'create_multiple_customer', CustomerController.add_multiple_customers, methods=['POST'])

