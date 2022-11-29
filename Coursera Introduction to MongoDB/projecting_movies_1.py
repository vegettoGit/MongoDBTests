# Coursera Introduction to MongoDB

import pymongo
from pymongo import MongoClient
import pprint
from IPython.display import clear_output

client = MongoClient("connectionString")

pipeline = [
    {
        '$limit': 10
    },
    {
        '$project': {
            'title': 1,
            'year': 1,
            'directors': {'$split': ["$director", ", "]},
            'actors': {'$split': ["$cast", ", "]},
            'writers': {'$split': ["$writer", ", "]},
            'genres': {'$split': ["$genre", ", "]},
            'languages': {'$split': ["$language", ", "]},
            'countries': {'$split': ["$country", ", "]},
            'plot': 1,
            'fullPlot': "$fullplot",
            'rated': "$rating",
            'released': 1,
            'runtime': 1,
            'poster': 1,
            'imdb': {
                'id': "$imdbID",
                'rating': "$imdbRating",
                'votes': "$imdbVotes"
                },
            'metacritic': 1,
            'awards': 1,
            'type': 1,
            'lastUpdated': "$lastupdated"
        }
    },
    {
        '$out': "movies_scratch"
    }
]

clear_output()
pprint.pprint(list(client.mflix.movies_initial.aggregate(pipeline)))