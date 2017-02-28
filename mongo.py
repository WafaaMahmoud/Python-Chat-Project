from pymongo import MongoClient
client = MongoClient()
db = client['pro']
coll = db['group']
cursor = db.user.find()
for document in cursor:
    print(document)