from app.auth.domain.models import Establishment
from app import db
from sqlalchemy import text



class EstablishmentDAO:
    @staticmethod
    def get_establishments_by_id(establishment_id):
        establishment = db.session.query(Establishment).get(establishment_id)
        return establishment

    @staticmethod
    def get_all_establishments():
        establishments = db.session.query(Establishment).all()
        return establishments

    @staticmethod
    def create_establishment(establishment_data):
        establishment = Establishment(**establishment_data)
        db.session.add(establishment)
        db.session.commit()
        return establishment

    @staticmethod
    def update_establishment(establishment, establishment_data):
        for key, value in establishment_data.items():
            setattr(establishment, key, value)
        db.session.commit()
        return establishment

    @staticmethod
    def delete_establishment(establishment):
        db.session.delete(establishment)
        db.session.commit()

    @staticmethod
    def get_max_rating_establishment():
        try:
            sql = text("CALL find_establishments_with_max_rating()")
            result = db.session.execute(sql)
            establishments = result.fetchall()

            establishments_list = [
                {column: value for column, value in zip(result.keys(), row)} for row in establishments
            ]

            return {
                "message": "Establishments with the highest rating retrieved successfully",
                "data": establishments_list
            }

        except Exception as e:
            db.session.rollback()
            print(e)
            return False

    @staticmethod
    def create_random_establishment_tables():
        try:
            sql = text("CALL create_random_establishment_tables()")
            db.session.execute(sql)

            result = db.session.execute(text(
                "SELECT table_name FROM information_schema.tables WHERE table_name LIKE 'RandomEstablishmentTable%' ORDER BY create_time DESC LIMIT 2"))
            tables = [row[0] for row in result.fetchall()]

            return {
                "message": "Random establishment tables created successfully",
                "tables": tables
            }

        except Exception as e:
            db.session.rollback()
            return False