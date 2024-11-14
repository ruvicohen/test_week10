import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(verbose=True)

DB_URL = os.environ['MONGO_URL']
client = MongoClient(DB_URL)

db = client['enemy_email']
all_messages = db['messages']
