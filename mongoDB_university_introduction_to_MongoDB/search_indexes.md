```
atlas clusters search indexes create --clusterName myAtlasClusterEDU -f /app/search_index.json
```

### Note that the content of search_index.json is:
```
{
    "name": "sample_supplies-sales-dynamic",
    "searchAnalyzer": "lucene.standard",
    "analyzer": "lucene.standard",
    "collectionName": "sales",
    "database": "sample_supplies",
    "mappings": {
        "dynamic": true
    }
}
```

### Returned result
```
Index sample_supplies-sales-dynamic created.
```

### Let's verify the index was created correctly
```
atlas clusters search indexes list --clusterName myAtlasClusterEDU --db sample_supplies --collection sales
```

### Returned result
```
ID                         NAME                            DATABASE          COLLECTION
63e2a9f65397a21d89b34926   sample_supplies-sales-dynamic   sample_supplies   sales
```

### Now we connect to the Atlas Cluster (replacing the user, password and connection string fields)
```
mongosh -u myAtlasDBUser -p myatlas-001 $MY_ATLAS_CONNECTION_STRING/sample_supplies


### Now we create an aggregation pipeline
```
db.sales.aggregate([
  {
    $search: {
      index: 'sample_supplies-sales-dynamic',
      text: {
        query: 'notepad', path: { 'wildcard': '*' }
      } } },
  {
    $set: {
      score: { $meta: "searchScore" }
      }
  }
])
```

