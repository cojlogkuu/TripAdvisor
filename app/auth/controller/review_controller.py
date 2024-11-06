from flask import jsonify, request
from app.auth.service.review_service import ReviewService

class ReviewController:
    @staticmethod
    def get_review(review_id):
        review = ReviewService.get_review_by_id(review_id)
        return jsonify(review) if review else (jsonify({'message': 'Review not found.'}), 404)

    @staticmethod
    def get_all_reviews():
        customer_id = request.args.get('customer_id')
        establishment_id = request.args.get('establishment_id')

        if customer_id:
            reviews = ReviewService.get_customer_reviews(customer_id)
            return jsonify(reviews)

        if establishment_id:
            reviews = ReviewService.get_establishment_reviews(establishment_id)
            return jsonify(reviews)

        reviews = ReviewService.get_all_reviews()
        return jsonify(reviews)

    @staticmethod
    def create_review():
        review_data = request.json
        review = ReviewService.create_review(review_data)
        return jsonify(review), 201

    @staticmethod
    def update_review(review_id):
        update_data = request.json
        review = ReviewService.update_review(review_id, update_data)
        return jsonify(review) if review else (jsonify({'message': 'Review not found.'}), 404)

    @staticmethod
    def delete_review(review_id):
        success = ReviewService.delete_review(review_id)
        return (jsonify(success), 204) if success else (jsonify({'message': 'Review not found.'}), 404)

