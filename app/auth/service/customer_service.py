from app.auth.dao.customer_dao import CustomerDAO

class CustomerService:
    @staticmethod
    def get_customer_by_id(customer_id):
        customer = CustomerDAO.get_customer_by_id(customer_id)
        if customer:
            return customer.to_dict()

    @staticmethod
    def get_all_customers():
        customers = CustomerDAO.get_all_customers()
        return [customer.to_dict() for customer in customers]

    @staticmethod
    def create_customer(customer_data):
        customer = CustomerDAO.create_customer(customer_data)
        return customer.to_dict()

    @staticmethod
    def update_customer(customer_id, update_data):
        customer = CustomerDAO.get_customer_by_id(customer_id)
        if customer:
            return CustomerDAO.update_customer(customer, update_data)
        return None

    @staticmethod
    def delete_customer(customer_id):
        customer = CustomerDAO.get_customer_by_id(customer_id)
        if customer:
            CustomerDAO.delete_customer(customer)
            return {'message': f'Customer with id {customer_id} deleted.'}
        else:
            return False

    @staticmethod
    def get_with_favorites():
        customers = CustomerDAO.get_favourites_establishments()
        return [customer.to_dict(include_favorities=True) for customer in customers]

    @staticmethod
    def add_favourites_establishment(customer, establishment):
        return CustomerDAO.add_favourites_establishment(customer, establishment)

    @staticmethod
    def add_multiple_customers():
        return CustomerDAO.add_multiple_customers()



