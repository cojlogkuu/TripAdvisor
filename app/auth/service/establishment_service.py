from app.auth.dao.establishment_dao import EstablishmentDAO

class EstablishmentService:
    @staticmethod
    def get_establishment_by_id(establishment_id):
         establishment = EstablishmentDAO.get_establishments_by_id(establishment_id)
         if establishment:
             return establishment.to_dict()

    @staticmethod
    def def_all_establishments():
        establishments = EstablishmentDAO.get_all_establishments()
        return [establishment.to_dict() for establishment in establishments]

    @staticmethod
    def create_establishment(establishment_data):
        return EstablishmentDAO.create_establishment(establishment_data).to_dict()

    @staticmethod
    def update_establishment(establishment_id, establishment_data):
        establishment = EstablishmentDAO.get_establishments_by_id(establishment_id)
        if establishment:
            return EstablishmentDAO.update_establishment(establishment, establishment_data).to_dict()
        return None

    @staticmethod
    def delete_establishment(establishment_id):
        establishment = EstablishmentDAO.get_establishments_by_id(establishment_id)
        if establishment:
            EstablishmentDAO.delete_establishment(establishment)
            return {'message': f'Establishment with id {establishment_id} deleted.'}
        else:
            return False