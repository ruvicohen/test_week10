import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database

load_dotenv(verbose=True)

database_url = os.environ['POSTGRES_URL']
engine = create_engine(database_url)
session_maker = sessionmaker(bind=engine)

Base = declarative_base()

def create_db():
    if not database_exists(engine.url):
        create_database(engine.url)