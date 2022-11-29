# Coursera Introduction to MongoDB

from pymongo import MongoClient

import pprint

# the connection uri to our cluster
client = MongoClient('connectionString')

# the trips collection on the citibike database
trips = client.citibike.trips

# find all trips between 5 and 10 minutes in duration that start at station 216
query = {"tripduration":{"$gte":5000,"$lt":10000},"start station id":216}

# only return the bikeid, tripduration, and _id (displayed by default)
projection = {"bikeid": 1, "tripduration": 1}

# print all of the trips
for doc in trips.find(query, projection):
    pprint.pprint(doc)