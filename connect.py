from pymongo import MongoClient

client = MongoClient("ConnectionStringWith_User_And_Password_AND_DatabaseName")

print(client.databaseName)