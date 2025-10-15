from flask import jsonify, request
from app.auth.service.establishment_service import EstablishmentService
from app.auth.utils.jwt_utils import token_required

class EstablishmentController:
    @staticmethod
    @token_required
    def get_establishment(establishment_id):
        """
        Get an establishment by ID
        ---
        tags:
          - Establishments
        security:
          - Bearer: []
        parameters:
          - name: establishment_id
            in: path
            type: integer
            required: true
            description: The ID of the establishment
        responses:
          200:
            description: Establishment details
            schema:
              type: object
              properties:
                id:
                  type: integer
                name:
                  type: string
                category_establishment_id:
                  type: integer
                street:
                  type: string
                city_id:
                  type: integer
                rating:
                  type: number
                owner_id:
                  type: integer
            examples:
              application/json:
                id: 1
                name: "Pizza Palace"
                category_establishment_id: 2
                street: "123 Main St"
                city_id: 1
                rating: 4.5
                owner_id: 1
          404:
            description: Establishment not found
            examples:
              application/json:
                message: "Establishment not found."
        """
        establishment = EstablishmentService.get_establishment_by_id(establishment_id)
        return jsonify(establishment) if establishment else (jsonify({'message': 'Establishment not found.'}), 404)

    @staticmethod
    @token_required
    def get_all_establishments():
        """
        Get all establishments
        ---
        tags:
          - Establishments
        security:
          - Bearer: []
        responses:
          200:
            description: List of all establishments
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  name:
                    type: string
                  category_establishment_id:
                    type: integer
                  street:
                    type: string
                  city_id:
                    type: integer
                  rating:
                    type: number
                  owner_id:
                    type: integer
            examples:
              application/json:
                - id: 1
                  name: "Pizza Palace"
                  category_establishment_id: 2
                  street: "123 Main St"
                  city_id: 1
                  rating: 4.5
                  owner_id: 1
        """
        establishments = EstablishmentService.def_all_establishments()
        return jsonify(establishments)

    @staticmethod
    @token_required
    def create_establishment():
        """
        Create a new establishment
        ---
        tags:
          - Establishments
        security:
          - Bearer: []
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              required:
                - name
                - category_establishment_id
                - street
                - city_id
              properties:
                name:
                  type: string
                  example: "Burger House"
                category_establishment_id:
                  type: integer
                  example: 1
                street:
                  type: string
                  example: "456 Oak Ave"
                city_id:
                  type: integer
                  example: 2
                rating:
                  type: number
                  example: 4.0
                owner_id:
                  type: integer
                  example: 3
            example:
              name: "Burger House"
              category_establishment_id: 1
              street: "456 Oak Ave"
              city_id: 2
              rating: 4.0
              owner_id: 3
        responses:
          201:
            description: Establishment created successfully
            schema:
              type: object
            examples:
              application/json:
                id: 5
                name: "Burger House"
                category_establishment_id: 1
                street: "456 Oak Ave"
                city_id: 2
                rating: 4.0
                owner_id: 3
          400:
            description: Invalid input
            examples:
              application/json:
                message: "Invalid input"
        """
        establishment_data = request.json
        establishment = EstablishmentService.create_establishment(establishment_data)
        return jsonify(establishment), 201

    @staticmethod
    @token_required
    def update_establishment(establishment_id):
        """
        Update an establishment by ID
        ---
        tags:
          - Establishments
        security:
          - Bearer: []
        parameters:
          - name: establishment_id
            in: path
            type: integer
            required: true
            description: The ID of the establishment to update
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                  example: "Updated Restaurant Name"
                category_establishment_id:
                  type: integer
                  example: 2
                street:
                  type: string
                  example: "789 New Street"
                city_id:
                  type: integer
                  example: 3
                rating:
                  type: number
                  example: 4.8
                owner_id:
                  type: integer
                  example: 2
            example:
              name: "Updated Restaurant Name"
              rating: 4.8
        responses:
          200:
            description: Establishment updated successfully
            schema:
              type: object
            examples:
              application/json:
                id: 1
                name: "Updated Restaurant Name"
                category_establishment_id: 2
                street: "123 Main St"
                city_id: 1
                rating: 4.8
                owner_id: 1
          404:
            description: Establishment not found
            examples:
              application/json:
                message: "Establishment not found."
        """
        update_data = request.json
        establishment = EstablishmentService.update_establishment(establishment_id, update_data)
        return jsonify(establishment) if establishment else (jsonify({'message': 'Establishment not found.'}), 404)

    @staticmethod
    @token_required
    def delete_establishment(establishment_id):
        """
        Delete an establishment by ID
        ---
        tags:
          - Establishments
        security:
          - Bearer: []
        parameters:
          - name: establishment_id
            in: path
            type: integer
            required: true
            description: The ID of the establishment to delete
        responses:
          204:
            description: Establishment deleted successfully
            examples:
              application/json:
                message: "Establishment deleted."
          404:
            description: Establishment not found
            examples:
              application/json:
                message: "Establishment not found."
        """
        success = EstablishmentService.delete_establishment(establishment_id)
        return (jsonify(success), 204) if success else (jsonify({'message': 'Establishment not found.'}), 404)

    @staticmethod
    @token_required
    def get_max_rating_establishment():
        """
        Get establishments with maximum rating using stored procedure
        ---
        tags:
          - Establishments
        security:
          - Bearer: []
        responses:
          201:
            description: Establishments with highest rating
            schema:
              type: object
            examples:
              application/json:
                establishments:
                  - id: 1
                    name: "Top Restaurant"
                    rating: 5.0
          404:
            description: Error executing stored procedure
            examples:
              application/json:
                message: "Error executing stored procedure."
        """
        result = EstablishmentService.get_max_rating_establishment()
        if result:
            return jsonify(result), 201
        else:
            return jsonify({'message': 'Error executing stored procedure.'}), 404

    @staticmethod
    @token_required
    def create_random_establishment_tables():
        """
        Create random establishment tables using stored procedure
        ---
        tags:
          - Establishments
        security:
          - Bearer: []
        responses:
          201:
            description: Random establishment tables created successfully
            schema:
              type: object
            examples:
              application/json:
                message: "Random tables created successfully"
          404:
            description: Error executing stored procedure
            examples:
              application/json:
                message: "Error executing stored procedure."
        """
        result = EstablishmentService.create_random_establishment_tables()
        if result:
            return jsonify(result), 201
        else:
            return jsonify({'message': 'Error executing stored procedure.'}), 404