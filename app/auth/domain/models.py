from sqlalchemy import Column, DECIMAL, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CategoryEstablishment(Base):
    __tablename__ = 'category_establishment'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(60), nullable=False, index=True)
    phone = Column(String(15))

    favourites_establishments = relationship('Establishment', secondary='favourites_establishment', cascade="all, delete-orphan", single_parent=True)
    reviews = relationship('Review', back_populates='customer', cascade="all, delete-orphan")
    security = relationship('Security', back_populates='customer')

    def to_dict(self, include_favorities=False):
        data =  {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }

        if include_favorities:
            data['favourites_establishments'] = [est.to_dict() for est in self.favourites_establishments]

        return data

class Security(Customer):
    __tablename__ = 'security'

    customer_id = Column(ForeignKey('customer.id', ondelete='CASCADE'), primary_key=True)
    password = Column(String(20), nullable=False)

    customer = relationship('Customer', back_populates='security', cascade="all, delete-orphan", single_parent=True)


class Owner(Base):
    __tablename__ = 'owner'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)
    phone = Column(String(15))


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    country_id = Column(ForeignKey('country.id'), nullable=False, index=True)

    country = relationship('Country')


class Establishment(Base):
    __tablename__ = 'establishment'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, index=True)
    category_establishment_id = Column(ForeignKey('category_establishment.id'), nullable=False, index=True)
    street = Column(String(100), nullable=False)
    city_id = Column(ForeignKey('city.id'), nullable=False, index=True)
    rating = Column(DECIMAL(3, 1))
    owner_id = Column(ForeignKey('owner.id'), index=True)

    category_establishment = relationship('CategoryEstablishment')
    city = relationship('City')
    owner = relationship('Owner')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category_establishment_id": self.category_establishment_id,
            "street": self.street,
            "city_id": self.city_id,
            "rating": self.rating,
            "owner_id": self.owner_id,
        }


t_favourites_establishment = Table(
    'favourites_establishment', metadata,
    Column('customer_id', ForeignKey('customer.id', ondelete='CASCADE'), primary_key=True, nullable=False),
    Column('establishment_id', ForeignKey('establishment.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True)
    url = Column(String(200), nullable=False)
    establishment_id = Column(ForeignKey('establishment.id'), nullable=False, index=True)

    establishment = relationship('Establishment')


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'), nullable=False, index=True)
    establishment_id = Column(ForeignKey('establishment.id'), nullable=False, index=True)
    text = Column(Text)
    rating = Column(DECIMAL(3, 1), nullable=False)

    customer = relationship('Customer', back_populates='reviews')
    establishment = relationship('Establishment')

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "establishment_id": self.establishment_id,
            "text": self.text,
            "rating": self.rating,
        }
