import pymongo
from pymongo import MongoClient
import pprint
from IPython.display import clear_output

client = MongoClient("connectionString")

pipeline = [
    {
        '$group': {
            '_id': {"language": "$language"},
            'count': {'$sum': 1}
        }
    },
    {
        '$sort': {'count':-1}
    }
]

clear_output()
pprint.pprint(list(client.mflix.movies_initial.aggregate(pipeline)))