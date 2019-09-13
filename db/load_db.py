# Loads the TextMD database
# Only needs to be run to refresh data or to initiate a new cluster
# Must be run from the db directory

import json
import pymongo
import db.db_connection_string as secrets

client = pymongo.MongoClient(secrets.MONGODB_CONNECTION_STRING)
db = client["textmd"]

def load_db(col, file):
    col = db[col]
    with open(file) as f:
        data = json.load(f)
    
    x = col.delete_many({})
    x = col.insert_many(data)

load_db("body", './locations.JSON')
load_db("symptoms", './symptoms.JSON')
