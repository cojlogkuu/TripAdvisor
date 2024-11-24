from app.auth.domain.models import Review
from app import db
from sqlalchemy import text as sql_text


class ReviewDAO:
    @staticmethod
    def get_review_by_id(review_id):
        review = db.session.query(Review).get(review_id)
        return review

    @staticmethod
    def get_all_reviews():
        reviews = db.session.query(Review).all()
        return reviews

    @staticmethod
    def get_customer_reviews(customer_id):
        reviews = db.session.query(Review).filter_by(customer_id=customer_id).all()
        return reviews

    @staticmethod
    def get_establishment_reviews(establishment_id):
        reviews = db.session.query(Review).filter_by(establishment_id=establishment_id).all()
        return reviews

    @staticmethod
    def create_review(review_data):
        review = Review(**review_data)
        db.session.add(review)
        db.session.commit()
        return review

    @staticmethod
    def update_review(review, review_data):
        for key, value in review_data.items():
            setattr(review, key, value)
        db.session.commit()
        return review

    @staticmethod
    def delete_review(review):
        db.session.delete(review)
        db.session.commit()

    @staticmethod
    def insert_review_using_procedure(customer_id, establishment_id, text, rating):
        try:
            sql = sql_text("CALL insert_review(:customer_id, :establishment_id, :text, :rating)")
            db.session.execute(sql,
                {
                    'customer_id': customer_id,
                    'establishment_id': establishment_id,
                    'text': text,
                    'rating': rating
                }
            )
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error executing stored procedure: {e}")
            return False
