from flask import Blueprint
from app.auth.controller.establishment_controller import EstablishmentController

establishment_bp = Blueprint('establishment', __name__)

establishment_bp.add_url_rule('/establishments/<int:establishment_id>', 'get_establishment', EstablishmentController.get_establishment, methods=['GET'])
establishment_bp.add_url_rule('/establishments', 'get_all_establishments', EstablishmentController.get_all_establishments, methods=['GET'])
establishment_bp.add_url_rule('/establishments', 'create_establishment', EstablishmentController.create_establishment, methods=['POST'])
establishment_bp.add_url_rule('/establishments/<int:establishment_id>', 'update_establishment', EstablishmentController.update_establishment, methods=['PUT'])
establishment_bp.add_url_rule('/establishments/<int:establishment_id>', 'delete_establishment', EstablishmentController.delete_establishment, methods=['DELETE'])