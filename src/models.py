import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False) 
    crew = Column(String(250), nullable=False) 
    passengers = Column(String(250), nullable=False) 
    max_atmosphering_speed = Column(String(250), nullable=False) 
    cargo_capacity = Column(String(250), nullable=False) 
    consumables = Column(String(250), nullable=False) 
    films = Column(Integer, ForeignKey('VehicleFilm'))
    pilots = Column(Integer, ForeignKey('PilotPeople'))
    url = Column(String(250), nullable=False) 
    created = Column(String(250), nullable=False) 
    edited = Column(String(250), nullable=False) 


class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False) 
    classification = Column(String(250), nullable=False) 
    designation = Column(String(250), nullable=False) 
    average_height = Column(String(250), nullable=False) 
    average_lifespan = Column(String(250), nullable=False) 
    eye_colors = Column(String(250), nullable=False) 
    hair_colors = Column(String(250), nullable=False) 
    skin_colors = Column(String(250), nullable=False)
    language = Column(String(250), nullable=False) 
    homeworld = Column(String(250), nullable=False) 
    people = Column(Integer, ForeignKey('people.id'))
    films = Column(Integer, ForeignKey('speciesfilm'))
    url = Column(String(250), nullable=False) 
    created = Column(String(250), nullable=False) 
    edited = Column(String(250), nullable=False) 


class PilotPeople(Base):
    __tablename__ = 'pilotpeople'
    pilot_id = Column(Integer, ForeignKey('people.id'))


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False) 
    birth_year =  Column(String(250), nullable=False) 
    eye_color = Column(String(250), nullable=False) 
    gender = Column(String(250), nullable=False) 
    hair_color = Column(String(250), nullable=False) 
    height = Column(String(250), nullable=False) 
    mass = Column(String(250), nullable=False) 
    skin_color = Column(String(250), nullable=False) 
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    planet_resident_id = Column(Integer, ForeignKey('planets.id'))
    species = Column(Integer, ForeignKey('PeopleSpecies'))
    starships = Column(Integer, ForeignKey('PeopleStarships'))
    vehicles = Column(Integer, ForeignKey('PeopleVehicles')) 
    url = Column(String(250), nullable=False) 
    created = Column(String(250), nullable=False) 
    edited = Column(String(250), nullable=False) 

class PeopleSpecies(Base):
    __tablename__ = 'peoplespecies'
    people = relationship(People)


class PeopleStarships(Base):
    __tablename__ = 'peoplestarships'
    people = relationship(People)
    


class PeopleVehicles(Base):
    __tablename__ = 'peoplevehicles'
    people = relationship(People)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name =  Column(String(250), nullable=False) 
    diameter = Column(String(250), nullable=False) 
    rotation_period = Column(String(250), nullable=False) 
    orbital_period = Column(String(250), nullable=False) 
    gravity = Column(String(250), nullable=False) 
    population = Column(String(250), nullable=False) 
    climate = Column(String(250), nullable=False) 
    terrain = Column(String(250), nullable=False) 
    surface_water = Column(String(250), nullable=False) 
    films = Column(Integer, ForeignKey('films'))
    url = Column(String(250), nullable=False) 
    # created = Date
    # edited = Date


class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False) 
    # episode_id = Column(Integer, ForeignKey())
    opening_crawl = Column(String(250), nullable=False) 
    director = Column(String(250), nullable=False) 
    producer = Column(String(250), nullable=False) 
    # release_date = Date
    # species = Column(Integer, ForeignKey('species.id'))
    starships = Column(Integer, ForeignKey('starship.id'))
    vehicles = Column(Integer, ForeignKey('vehicle.id'))
    planets = Column(Integer, ForeignKey('planets.id'))
    url = Column(String(250), nullable=False) 
    # created = Date
    # edited = Date


class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name =  Column(String(250), nullable=False) 
    model = Column(String(250), nullable=False) 
    starship_class = Column(String(250), nullable=False) 
    manufacturer = Column(String(250), nullable=False) 
    cost_in_credits = Column(String(250), nullable=False) 
    length = Column(String(250), nullable=False) 
    crew = Column(String(250), nullable=False) 
    passengers = Column(String(250), nullable=False) 
    max_atmosphere_speed = Column(String(250), nullable=False) 
    hyperdrive_rating = Column(String(250), nullable=False) 
    MGLT = Column(String(250), nullable=False) 
    cargo_capacity = Column(String(250), nullable=False) 
    consumables = Column(String(250), nullable=False) 
    films = Column(String(250), nullable=False) 
    pilots = Column(String(250), nullable=False) 
    url = Column(String(250), nullable=False) 
    created = Column(String(250), nullable=False) 
    edited = Column(String(250), nullable=False) 





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')