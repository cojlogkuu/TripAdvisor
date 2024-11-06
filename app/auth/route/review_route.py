from flask import Blueprint
from app.auth.controller.review_controller import ReviewController

review_bp = Blueprint('review', __name__)

review_bp.add_url_rule('/reviews/<int:review_id>', 'get_review', ReviewController.get_review, methods=['GET'])
review_bp.add_url_rule('/reviews', 'get_all_reviews', ReviewController.get_all_reviews, methods=['GET'])
review_bp.add_url_rule('/reviews/<int:review_id>', 'update_review', ReviewController.update_review, methods=['PUT'])
review_bp.add_url_rule('/reviews', 'create_review', ReviewController.create_review, methods=['POST'])
review_bp.add_url_rule('/reviews/<int:review_id>', 'delete_review', ReviewController.delete_review, methods=['DELETE'])