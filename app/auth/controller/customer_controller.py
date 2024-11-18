from flask import jsonify, request
from app.auth.service.customer_service import CustomerService

class CustomerController:
    @staticmethod
    def get_customer(customer_id):
        customer = CustomerService.get_customer_by_id(customer_id)
        return jsonify(customer) if customer else (jsonify({'message': 'Customer not found.'}), 404)

    @staticmethod
    def get_all_customers():
        customers = CustomerService.get_all_customers()
        return jsonify(customers)

    @staticmethod
    def create_customer():
        customer_data = request.json
        customer = CustomerService.create_customer(customer_data)
        return jsonify(customer), 201

    @staticmethod
    def update_customer(customer_id):
        update_data = request.json
        customer = CustomerService.update_customer(customer_id, update_data)
        return jsonify(customer) if customer else (jsonify({'message': 'Customer not found.'}), 404)

    @staticmethod
    def delete_customer(customer_id):
        success = CustomerService.delete_customer(customer_id)
        return (jsonify(success), 204) if success else (jsonify({'message': 'Customer not found.'}), 404)


    @staticmethod
    def get_favorite_customer():
        data = CustomerService.get_with_favorites()
        return jsonify(data)