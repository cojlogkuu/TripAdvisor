from app.auth.dao.review_dao import ReviewDAO

class ReviewService:
    @staticmethod
    def get_review_by_id(request_id):
        review = ReviewDAO.get_review_by_id(request_id)
        if review:
            return review.to_dict()

    @staticmethod
    def get_all_reviews():
        review = ReviewDAO.get_all_reviews()
        return [review.to_dict() for review in review]

    @staticmethod
    def get_customer_reviews(customer_id):
        reviews = ReviewDAO.get_customer_reviews(customer_id)
        if reviews:
            return [review.to_dict() for review in reviews]

    @staticmethod
    def get_establishment_reviews(establishment_id):
        reviews = ReviewDAO.get_establishment_reviews(establishment_id)
        if reviews:
            return [review.to_dict() for review in reviews]

    @staticmethod
    def create_review(review_data):
        return ReviewDAO.create_review(review_data).to_dict()

    @staticmethod
    def update_review(review_id, review_data):
        review = ReviewDAO.get_review_by_id(review_id)
        if review:
            return ReviewDAO.update_review(review, review_data).to_dict()
        return None

    @staticmethod
    def delete_review(request_id):
        review = ReviewDAO.get_review_by_id(request_id)
        if review:
            ReviewDAO.delete_review(review)
            return {'message': f'Review with id {request_id} deleted.'}
        else:
            return False

