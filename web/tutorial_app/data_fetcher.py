
from pymongo import MongoClient

def get_decibel_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['mydatabase']
    collection = db['sensor_data']
    data = collection.find_one({}, {'_id': 0, 'decibel': 1})
    decibel_value = data['decibel']
    return decibel_value

