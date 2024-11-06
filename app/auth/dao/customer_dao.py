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
