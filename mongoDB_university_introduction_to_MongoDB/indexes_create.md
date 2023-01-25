```
db.transfers.getIndexes()
```

### Returned result
```
[ { v: 2, key: { _id: 1 }, name: '_id_' } ]
```

```
db.accounts.createIndex({ account_id: 1 }, { unique: true })
```

### Returned result
```
account_id_1
```

```
db.accounts.explain().find({ account_id: "MDB829000996" })
```

### Returned result
```
{
  explainVersion: '1',
  queryPlanner: {
    namespace: 'bank.accounts',
    indexFilterSet: false,
    parsedQuery: { account_id: { '$eq': 'MDB829000996' } },
    queryHash: 'C7AD3977',
    planCacheKey: 'E975A254',
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    winningPlan: {
      stage: 'FETCH',
      inputStage: {
        stage: 'IXSCAN',
        keyPattern: { account_id: 1 },
        indexName: 'account_id_1',
        isMultiKey: false,
        multiKeyPaths: { account_id: [] },
        isUnique: false,
        isSparse: false,
        isPartial: false,
        indexVersion: 2,
        direction: 'forward',
        indexBounds: { account_id: [ '["MDB829000996", "MDB829000996"]' ] }
      }
    },
    rejectedPlans: []
  },
  command: {
    find: 'accounts',
    filter: { account_id: 'MDB829000996' },
    '$db': 'bank'
  },
  serverInfo: {
    host: 'atlas-d3opcw-shard-00-02.3xfvk.mongodb.net',
    port: 27017,
    version: '6.0.3',
    gitVersion: 'f803681c3ae19817d31958965850193de067c516'
  },
  serverParameters: {
    internalQueryFacetBufferSizeBytes: 104857600,
    internalQueryFacetMaxOutputDocSizeBytes: 104857600,
    internalLookupStageIntermediateDocumentMaxSizeBytes: 104857600,
    internalDocumentSourceGroupMaxMemoryBytes: 104857600,
    internalQueryMaxBlockingSortMemoryUsageBytes: 104857600,
    internalQueryProhibitBlockingMergeOnMongoS: 0,
    internalQueryMaxAddToSetBytes: 104857600,
    internalDocumentSourceSetWindowFieldsMaxMemoryBytes: 104857600
  },
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1674675668, i: 1 }),
    signature: {
      hash: Binary(Buffer.from("bf99edba756f33885d5cd99038b68308863379f3", "hex"), 0),
      keyId: Long("7154370897485234178")
    }
  },
  operationTime: Timestamp({ t: 1674675668, i: 1 })
}
```
