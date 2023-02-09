### Connect to the Atlas Cluster (replacing the user, password and connection string fields)
```
mongosh -u myAtlasDBUser -p myatlas-001 $MY_ATLAS_CONNECTION_STRING/sample_supplies
```

### Now we create an aggregation pipeline
```
db.sales.aggregate([
  {
    $search: {
      index: 'sample_supplies-sales-dynamic',
      "compound": {
        "filter": [
          {
            "text": {
              "query": "Online",
              "path": "purchaseMethod"
            }
          }
        ],
        "should": [
          {
            "text": {
              "query": "notepad",
              "path": "items",
              "score": { "constant": {"value": 5} }
            }
          }
      ]
      }
    }
  }
])
```


