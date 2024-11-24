from flask import jsonify, request
from app.auth.service.establishment_service import EstablishmentService

class EstablishmentController:
    @staticmethod
    def get_establishment(establishment_id):
        establishment = EstablishmentService.get_establishment_by_id(establishment_id)
        return jsonify(establishment) if establishment else (jsonify({'message': 'Establishment not found.'}), 404)

    @staticmethod
    def get_all_establishments():
        establishments = EstablishmentService.def_all_establishments()
        return jsonify(establishments)

    @staticmethod
    def create_establishment():
        establishment_data = request.json
        establishment = EstablishmentService.create_establishment(establishment_data)
        return jsonify(establishment), 201

    @staticmethod
    def update_establishment(establishment_id):
        update_data = request.json
        establishment = EstablishmentService.update_establishment(establishment_id, update_data)
        return jsonify(establishment) if establishment else (jsonify({'message': 'Establishment not found.'}), 404)

    @staticmethod
    def delete_establishment(establishment_id):
        success = EstablishmentService.delete_establishment(establishment_id)
        return (jsonify(success), 204) if success else (jsonify({'message': 'Establishment not found.'}), 404)

    @staticmethod
    def get_max_rating_establishment():
        result = EstablishmentService.get_max_rating_establishment()
        if result:
            return jsonify(result), 201
        else:
            return jsonify({'message': 'Error executing stored procedure.'}), 404

    @staticmethod
    def create_random_establishment_tables():
        result = EstablishmentService.create_random_establishment_tables()
        if result:
            return jsonify(result), 201
        else:
            return jsonify({'message': 'Error executing stored procedure.'}), 404