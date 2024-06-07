from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import configparser
import os

def init_database():
    config_file = os.path.join(os.getcwd(), 'python-playground\\api-playground\\config\\config.ini')

    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Config file '{config_file}' not found.")

    config = configparser.ConfigParser()

    config.read(config_file)

    if 'MongoDB' not in config:
        raise KeyError("Key 'MongoDB' not found in config file.")

    username = config['MongoDB']['username']
    password = config['MongoDB']['password']
    cluster = config['MongoDB']['cluster']
    app_name = config['MongoDB']['app_name']

    uri = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName={app_name}"

    client = MongoClient(uri)
    database = client["sample_restaurants"]
   
    return database

def init_restaurants_collection(database):
    restaurants_collection = database["restaurants"]
    return restaurants_collection

def init_neighborhoods_collection(database):
    neighborhoods_collection = database["neighborhoods"]
    return neighborhoods_collection
