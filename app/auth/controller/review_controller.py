from flask import jsonify, request
from app.auth.service.review_service import ReviewService
from app.auth.utils.jwt_utils import token_required

class ReviewController:
    @staticmethod
    @token_required
    def get_review(review_id):
        """
        Get a review by ID
        ---
        tags:
          - Reviews
        security:
          - Bearer: []
        parameters:
          - name: review_id
            in: path
            type: integer
            required: true
            description: The ID of the review
        responses:
          200:
            description: Review details
            schema:
              type: object
              properties:
                id:
                  type: integer
                customer_id:
                  type: integer
                establishment_id:
                  type: integer
                text:
                  type: string
                rating:
                  type: number
            examples:
              application/json:
                id: 1
                customer_id: 5
                establishment_id: 10
                text: "Great food and service!"
                rating: 4.5
          404:
            description: Review not found
            examples:
              application/json:
                message: "Review not found."
        """
        review = ReviewService.get_review_by_id(review_id)
        return jsonify(review) if review else (jsonify({'message': 'Review not found.'}), 404)

    @staticmethod
    @token_required
    def get_all_reviews():
        """
        Get all reviews with optional filters
        ---
        tags:
          - Reviews
        security:
          - Bearer: []
        parameters:
          - name: customer_id
            in: query
            type: integer
            required: false
            description: Filter reviews by customer ID
          - name: establishment_id
            in: query
            type: integer
            required: false
            description: Filter reviews by establishment ID
        responses:
          200:
            description: List of reviews
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  customer_id:
                    type: integer
                  establishment_id:
                    type: integer
                  text:
                    type: string
                  rating:
                    type: number
            examples:
              application/json:
                - id: 1
                  customer_id: 5
                  establishment_id: 10
                  text: "Great food and service!"
                  rating: 4.5
                - id: 2
                  customer_id: 3
                  establishment_id: 10
                  text: "Nice atmosphere"
                  rating: 4.0
        """
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
    @token_required
    def create_review():
        """
        Create a new review
        ---
        tags:
          - Reviews
        security:
          - Bearer: []
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              required:
                - customer_id
                - establishment_id
                - rating
              properties:
                customer_id:
                  type: integer
                  example: 5
                establishment_id:
                  type: integer
                  example: 10
                text:
                  type: string
                  example: "Amazing experience! Highly recommended."
                rating:
                  type: number
                  example: 5.0
            example:
              customer_id: 5
              establishment_id: 10
              text: "Amazing experience! Highly recommended."
              rating: 5.0
        responses:
          201:
            description: Review created successfully
            schema:
              type: object
            examples:
              application/json:
                id: 15
                customer_id: 5
                establishment_id: 10
                text: "Amazing experience! Highly recommended."
                rating: 5.0
          400:
            description: Invalid input
            examples:
              application/json:
                message: "Invalid input"
        """
        review_data = request.json
        review = ReviewService.create_review(review_data)
        return jsonify(review), 201

    @staticmethod
    @token_required
    def update_review(review_id):
        """
        Update a review by ID
        ---
        tags:
          - Reviews
        security:
          - Bearer: []
        parameters:
          - name: review_id
            in: path
            type: integer
            required: true
            description: The ID of the review to update
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                text:
                  type: string
                  example: "Updated review text"
                rating:
                  type: number
                  example: 4.8
            example:
              text: "Updated review text after revisit"
              rating: 4.8
        responses:
          200:
            description: Review updated successfully
            schema:
              type: object
            examples:
              application/json:
                id: 15
                customer_id: 5
                establishment_id: 10
                text: "Updated review text after revisit"
                rating: 4.8
          404:
            description: Review not found
            examples:
              application/json:
                message: "Review not found."
        """
        update_data = request.json
        review = ReviewService.update_review(review_id, update_data)
        return jsonify(review) if review else (jsonify({'message': 'Review not found.'}), 404)

    @staticmethod
    @token_required
    def delete_review(review_id):
        """
        Delete a review by ID
        ---
        tags:
          - Reviews
        security:
          - Bearer: []
        parameters:
          - name: review_id
            in: path
            type: integer
            required: true
            description: The ID of the review to delete
        responses:
          204:
            description: Review deleted successfully
            examples:
              application/json:
                message: "Review deleted."
          404:
            description: Review not found
            examples:
              application/json:
                message: "Review not found."
        """
        success = ReviewService.delete_review(review_id)
        return (jsonify(success), 204) if success else (jsonify({'message': 'Review not found.'}), 404)

    @staticmethod
    @token_required
    def create_review_procedure():
        """
        Create a review using stored procedure
        ---
        tags:
          - Reviews
        security:
          - Bearer: []
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              required:
                - customer_id
                - establishment_id
                - rating
              properties:
                customer_id:
                  type: integer
                  example: 5
                establishment_id:
                  type: integer
                  example: 10
                text:
                  type: string
                  example: "Review added via procedure"
                rating:
                  type: number
                  example: 4.5
            example:
              customer_id: 5
              establishment_id: 10
              text: "Review added via procedure"
              rating: 4.5
        responses:
          201:
            description: Review added using procedure
            examples:
              application/json:
                message: "Review was added using procedure."
          404:
            description: Error executing procedure
            examples:
              application/json:
                message: "Review was not added using procedure."
        """
        review_data = request.json
        customer_id = review_data.get('customer_id')
        establishment_id = review_data.get('establishment_id')
        text = review_data.get('text')
        rating = review_data.get('rating')
        result = ReviewService.create_review_procedure(customer_id, establishment_id, text, rating)
        if result:
            return jsonify({'message': 'Review was added using procedure.'}), 201
        else:
            return jsonify({'message': 'Review was not added using procedure.'}), 404

