from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.sis7sux.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'name':'yuyu',
    'age':31
}
db.users.insert_one(doc)
