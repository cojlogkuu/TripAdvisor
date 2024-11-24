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

    @staticmethod
    def add_favourites_establishment():
        data = request.json

        customer = data.get('customer')
        establishment = data.get('establishment')

        if not customer or not establishment:
            return jsonify({"message": "Both customer and establishment are required"}), 400

        result = CustomerService.add_favourites_establishment(customer, establishment)

        if result:
            return jsonify({"message": f"{establishment} was set as favourite for {customer}"}), 201
        else:
            return jsonify({"message": f"{establishment} was not set"}), 401

    @staticmethod
    def add_multiple_customers():
        result = CustomerService.add_multiple_customers()
        if result:
            return jsonify({"message": "Multiple customers were added."}), 201
        else:
            return jsonify({"message": f"Multiple customers were not added."}), 401