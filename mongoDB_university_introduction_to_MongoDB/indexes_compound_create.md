```
db.accounts.createIndex({
  account_holder: 1,
  balance: 1,
  account_type: 1
})
```

### Returned result
```
account_holder_1_balance_1_account_type_1
```

```
db.accounts.explain().find( { account_holder:"Andrea", balance:{ $gt:5 }}, { account_holder: 1, balance: 1, account_type:1, _id: 0}).sort({ balance: 1 })
```

### Returned result
```
{
  explainVersion: '1',
  queryPlanner: {
    namespace: 'bank.accounts',
    indexFilterSet: false,
    parsedQuery: {
      '$and': [
        { account_holder: { '$eq': 'Andrea' } },
        { balance: { '$gt': 5 } }
      ]
    },
    queryHash: 'AD6630BF',
    planCacheKey: '4DDA3952',
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    winningPlan: {
      stage: 'PROJECTION_COVERED',
      transformBy: { account_holder: 1, balance: 1, account_type: 1, _id: 0 },
      inputStage: {
        stage: 'IXSCAN',
        keyPattern: { account_holder: 1, balance: 1, account_type: 1 },
        indexName: 'account_holder_1_balance_1_account_type_1',
        isMultiKey: false,
        multiKeyPaths: { account_holder: [], balance: [], account_type: [] },
        isUnique: false,
        isSparse: false,
        isPartial: false,
        indexVersion: 2,
        direction: 'forward',
        indexBounds: {
          account_holder: [ '["Andrea", "Andrea"]' ],
          balance: [ '(5, inf.0]' ],
          account_type: [ '[MinKey, MaxKey]' ]
        }
      }
    },
    rejectedPlans: []
  },
  command: {
    find: 'accounts',
    filter: { account_holder: 'Andrea', balance: { '$gt': 5 } },
    sort: { balance: 1 },
    projection: { account_holder: 1, balance: 1, account_type: 1, _id: 0 },
    '$db': 'bank'
  },
  serverInfo: {
    host: 'atlas-d3opcw-shard-00-02.3xfvk.mongodb.net',
    port: 27017,
    version: '6.0.4',
    gitVersion: '44ff59461c1353638a71e710f385a566bcd2f547'
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
    clusterTime: Timestamp({ t: 1675353194, i: 1 }),
    signature: {
      hash: Binary(Buffer.from("cacc66a895bf1d26ccba5d027fcc158c30cfaf48", "hex"), 0),
      keyId: Long("7154370897485234178")
    }
  },
  operationTime: Timestamp({ t: 1675353194, i: 1 })
}
```

