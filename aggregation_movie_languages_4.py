import pymongo
from pymongo import MongoClient
import pprint
from IPython.display import clear_output

client = MongoClient("connectionString")

pipeline = [
    {
        '$sortByCount': "$language"
    },
    {
        '$facet': {
            'top language combinations': [{'$limit': 100}],
            'unusual combinations shared by': [{
                '$skip': 100
            },
            {
                '$bucketAuto': {
                    'groupBy': "$count",
                    'buckets': 5,
                    'output': {
                        'language combinations': {'$sum': 1}
                    }
                }
            }]
        }
    }
]

clear_output()
pprint.pprint(list(client.mflix.movies_initial.aggregate(pipeline)))