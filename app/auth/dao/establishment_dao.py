from app.auth.domain.models import Establishment
from app import db


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