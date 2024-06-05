from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import configparser
import os

config_file = os.path.join(os.getcwd(), 'python-playground\\api-playground\\config\\config.ini')

if not os.path.exists(config_file):
    raise FileNotFoundError(f"Config file '{config_file}' not found.")

config = configparser.ConfigParser()

config.read(config_file)

if 'MongoDB' not in config:
    raise KeyError("Ney 'MongoDB' not found in config file.")

username = config['MongoDB']['username']
password = config['MongoDB']['password']
db_adress = config['MongoDB']['database_adress']
app_name = config['MongoDB']['app_name']

uri = f"mongodb+srv://{username}:{password}@{db_adress}/?retryWrites=true&w=majority&appName={app_name}"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)