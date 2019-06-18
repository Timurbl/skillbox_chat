from pymongo import MongoClient
client = MongoClient('mongodb+srv://timurbl:#wb8YIyGuhmrEbSYC@cluster0-f09gd.mongodb.net/test')
dbUsers = client.users
dbUsers.insertOne({
    "name": "Timur"
})