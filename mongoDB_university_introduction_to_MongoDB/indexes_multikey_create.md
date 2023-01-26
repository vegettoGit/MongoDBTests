```
db.accounts.createIndex({ transfers_complete: 1 })
```

### Returned result
```
transfers_complete_1
```

```
db.accounts.explain().find({ transfers_complete: { $in: ["TR617907396"] } })
```

### Returned result
```
{
  explainVersion: '1',
  queryPlanner: {
    namespace: 'bank.accounts',
    indexFilterSet: false,
    parsedQuery: { transfers_complete: { '$eq': 'TR617907396' } },
    queryHash: 'D341FD99',
    planCacheKey: '061129EA',
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    winningPlan: {
      stage: 'FETCH',
      inputStage: {
        stage: 'IXSCAN',
        keyPattern: { transfers_complete: 1 },
        indexName: 'transfers_complete_1',
        isMultiKey: true,
        multiKeyPaths: { transfers_complete: [ 'transfers_complete' ] },
        isUnique: false,
        isSparse: false,
        isPartial: false,
        indexVersion: 2,
        direction: 'forward',
        indexBounds: { transfers_complete: [ '["TR617907396", "TR617907396"]' ] }
      }
    },
    rejectedPlans: []
  },
  command: {
    find: 'accounts',
    filter: { transfers_complete: { '$in': [ 'TR617907396' ] } },
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
    clusterTime: Timestamp({ t: 1674761865, i: 7 }),
    signature: {
      hash: Binary(Buffer.from("a7af6e939c283cd4b48d268a6de6b2cd637d804c", "hex"), 0),
      keyId: Long("7154370897485234178")
    }
  },
  operationTime: Timestamp({ t: 1674761865, i: 7 })
}
```

