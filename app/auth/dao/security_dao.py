from app import db
from app.auth.domain.models import Security

class SecurityDAO:
    @staticmethod
    def create_security(security_data):
        """Create a new security record"""
        security = Security(**security_data)
        db.session.add(security)
        db.session.commit()
        return security

    @staticmethod
    def get_security_by_customer_id(customer_id):
        """Get security record by customer ID"""
        return db.session.query(Security).filter_by(customer_id=customer_id).first()

    @staticmethod
    def update_security(customer_id, update_data):
        """Update security record"""
        security = SecurityDAO.get_security_by_customer_id(customer_id)
        if security:
            for key, value in update_data.items():
                setattr(security, key, value)
            db.session.commit()
            return security
        return None

    @staticmethod
    def delete_security(customer_id):
        """Delete security record"""
        security = SecurityDAO.get_security_by_customer_id(customer_id)
        if security:
            db.session.delete(security)
            db.session.commit()
            return True
        return False
