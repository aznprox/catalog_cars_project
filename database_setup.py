import sys 

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Make(Base):
    __tablename__ = 'make'

    name = Column(
    String(80), nullable = False)

    image = Column(
    String(80), nullable = False)

    id = Column(
    Integer, primary_key = True)

class Model(Base):
    __tablename__ = 'model'

    name = Column(
    String(80), nullable = False)

    id = Column(
    Integer, primary_key = True)

    image = Column(
    String(250))

    description = Column(
    String(250))

    price = Column(
    String(8))

    make_id = Column(
    Integer, ForeignKey('make.id'))

    make = relationship(Make)

# We added this serialize function to be able to send JSON objects in a
# serializable format
    @property
    def serialize(self):

        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'image': self.image,
        }
    
###### insert at end of file #####

engine = create_engine('sqlite:///carmake.db')

Base.metadata.create_all(engine)