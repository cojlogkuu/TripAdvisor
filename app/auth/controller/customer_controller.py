from flask import jsonify, request
from app.auth.service.customer_service import CustomerService

class CustomerController:
    @staticmethod
    def get_customer(customer_id):
        """
        Get a customer by ID
        ---
        tags:
          - Customers
        parameters:
          - name: customer_id
            in: path
            type: integer
            required: true
        responses:
          200:
            description: Customer details
            schema:
              type: object
            examples:
              application/json:
                id: 1
                name: "John Doe"
                email: "john@example.com"
          404:
            description: Customer not found
            examples:
              application/json:
                message: "Customer not found."
        """
        customer = CustomerService.get_customer_by_id(customer_id)
        return jsonify(customer) if customer else (jsonify({'message': 'Customer not found.'}), 404)

    @staticmethod
    def get_all_customers():
        """
        Get all customers
        ---
        tags:
          - Customers
        responses:
          200:
            description: List of customers
            schema:
              type: array
              items:
                type: object
            examples:
              application/json:
                - id: 1
                  name: "John Doe"
                  email: "john@example.com"
                - id: 2
                  name: "Jane Smith"
                  email: "jane@example.com"
        """
        customers = CustomerService.get_all_customers()
        return jsonify(customers)

    @staticmethod
    def create_customer():
        """
        Create a new customer
        ---
        tags:
          - Customers
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
            example:
              name: "John Doe"
              email: "john@example.com"
        responses:
          201:
            description: Customer created
            schema:
              type: object
            examples:
              application/json:
                id: 1
                name: "John Doe"
                email: "john@example.com"
          400:
            description: Invalid input
            examples:
              application/json:
                message: "Invalid input"
        """
        customer_data = request.json
        customer = CustomerService.create_customer(customer_data)
        return jsonify(customer), 201

    @staticmethod
    def update_customer(customer_id):
        """
        Update a customer by ID
        ---
        tags:
          - Customers
        parameters:
          - name: customer_id
            in: path
            type: integer
            required: true
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                  example: "Jane Smith"
                email:
                  type: string
                  example: "jane@example.com"
            example:
              name: "Jane Smith"
              email: "jane@example.com"
        responses:
          200:
            description: Customer updated
            schema:
              type: object
            examples:
              application/json:
                id: 2
                name: "Jane Smith"
                email: "jane@example.com"
          404:
            description: Customer not found
            examples:
              application/json:
                message: "Customer not found."
        """
        update_data = request.json
        customer = CustomerService.update_customer(customer_id, update_data)
        return jsonify(customer) if customer else (jsonify({'message': 'Customer not found.'}), 404)

    @staticmethod
    def delete_customer(customer_id):
        """
        Delete a customer by ID
        ---
        tags:
          - Customers
        parameters:
          - name: customer_id
            in: path
            type: integer
            required: true
        responses:
          204:
            description: Customer deleted
            examples:
              application/json:
                message: "Customer deleted."
          404:
            description: Customer not found
            examples:
              application/json:
                message: "Customer not found."
        """
        success = CustomerService.delete_customer(customer_id)
        return (jsonify(success), 204) if success else (jsonify({'message': 'Customer not found.'}), 404)

    @staticmethod
    def get_favorite_customer():
        """
        Get customers with favorite establishments
        ---
        tags:
          - Customers
        responses:
          200:
            description: List of customers with favorites
            schema:
              type: array
              items:
                type: object
            examples:
              application/json:
                - id: 1
                  name: "John Doe"
                  favorites:
                    - id: 10
                      name: "Pizza Place"
                - id: 2
                  name: "Jane Smith"
                  favorites:
                    - id: 11
                      name: "Burger Joint"
        """
        data = CustomerService.get_with_favorites()
        return jsonify(data)

    @staticmethod
    def add_favourites_establishment():
        """
        Add favorite establishments for a customer
        ---
        tags:
          - Customers
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                customer:
                  type: string
                  example: "John Doe"
                establishment:
                  type: string
                  example: "Pizza Place"
            example:
              customer: "John Doe"
              establishment: "Pizza Place"
        responses:
          201:
            description: Favorites added
            examples:
              application/json:
                message: "Pizza Place was set as favourite for John Doe"
          400:
            description: Invalid input
            examples:
              application/json:
                message: "Both customer and establishment are required"
        """
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
        """
        Create multiple customers
        ---
        tags:
          - Customers
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: array
              items:
                type: object
                properties:
                  name:
                    type: string
                    example: "John Doe"
                  email:
                    type: string
                    example: "john@example.com"
            example:
              - name: "John Doe"
                email: "john@example.com"
              - name: "Jane Smith"
                email: "jane@example.com"
        responses:
          201:
            description: Multiple customers were added
            examples:
              application/json:
                message: "Multiple customers were added."
          401:
            description: Multiple customers were not added
            examples:
              application/json:
                message: "Multiple customers were not added."
        """
        result = CustomerService.add_multiple_customers()
        if result:
            return jsonify({"message": "Multiple customers were added."}), 201
        else:
            return jsonify({"message": f"Multiple customers were not added."}), 401