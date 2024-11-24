from flask import jsonify
from sqlalchemy.orm import joinedload
from sqlalchemy import text
from app.auth.domain.models import Customer
from app import db


class CustomerDAO:
    @staticmethod
    def get_customer_by_id(customer_id):
        customer = db.session.query(Customer).get(customer_id)
        return customer

    @staticmethod
    def get_all_customers():
        customers = db.session.query(Customer).all()
        return customers

    @staticmethod
    def create_customer(customer_data):
        customer = Customer(**customer_data)
        db.session.add(customer)
        db.session.commit()
        return customer.to_dict()

    @staticmethod
    def update_customer(customer, update_data):
        for key, value in update_data.items():
            setattr(customer, key, value)
        db.session.commit()
        return customer.to_dict()

    @staticmethod
    def delete_customer(customer):
        db.session.delete(customer)
        db.session.commit()

    @staticmethod
    def get_favourites_establishments():
         return db.session.query(Customer).options(
            joinedload(Customer.favourites_establishments)
        ).all()

    @staticmethod
    def add_favourites_establishment(customer, establishment):
        try:
            sql = text("""
                    CALL insert_favourite_establishment(:customer_name, :establishment_name)
                """)

            db.session.execute(sql, {
                'customer_name': customer,
                'establishment_name': establishment
            })

            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def add_multiple_customers():
        try:
            sql = text("CALL insert_multiple_customers()")
            db.session.execute(sql)
            db.session.commit()

            return True

        except Exception as e:
            db.session.rollback()
            return False