```
atlas clusters search indexes create --clusterName myAtlasClusterEDU -f /app/search_index.json
```

### Note that the content of search_index.json is:
```
{
    "name": "sample_supplies-sales-facets",
    "searchAnalyzer": "lucene.standard",
    "analyzer": "lucene.standard",
    "collectionName": "sales",
    "database": "sample_supplies",
    "mappings": {
      "dynamic": true,
      "fields": {
        "purchaseMethod": [
          {
            "dynamic": true,
            "type": "document"
          },
          {
            "type": "string"
          }
        ],
        "storeLocation": [
          {
            "dynamic": true,
            "type": "document"
          },
          {
            "type": "stringFacet"
          }
        ]
      }
    }
}
```

### Returned result
```
Index sample_supplies-sales-facets created.
```

### Let's verify the index was created correctly
```
atlas clusters search indexes list --clusterName myAtlasClusterEDU --db sample_supplies --collection sales
```

### Returned result
```
ID                         NAME                            DATABASE          COLLECTION
63e2a9f65397a21d89b34926   sample_supplies-sales-dynamic   sample_supplies   sales
640712e16cf7292818c59c11   sample_supplies-sales-facets    sample_supplies   sales
```

### Now we connect to the Atlas Cluster (replacing the user, password and connection string fields)
```
mongosh -u myAtlasDBUser -p myatlas-001 $MY_ATLAS_CONNECTION_STRING/sample_supplies
```

### Now we create an aggregation pipeline
```
db.sales.aggregate([
  {
    $searchMeta: {
      index: 'sample_supplies-sales-facets',
        "facet": {
            "operator": {
                "text": {
                    "query": ["In store"],
                    "path": "purchaseMethod"
                }
            },
            "facets": {
                "locationFacet": {
                    "type": "string",
                    "path": "storeLocation",
                }
            }
        }
    }
  }
])
```

### Results
```
[
  {
    count: { lowerBound: Long("2819") },
    facet: {
      locationFacet: {
        buckets: [
          { _id: 'Denver', count: Long("864") },
          { _id: 'Seattle', count: Long("648") },
          { _id: 'London', count: Long("455") },
          { _id: 'Austin', count: Long("378") },
          { _id: 'New York', count: Long("289") },
          { _id: 'San Diego', count: Long("185") }
        ]
      }
    }
  }
]
```
