```
db.accounts.dropIndex("account_holder_1")
```

### Returned result
```
{
  nIndexesWas: 2,
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1675683048, i: 1 }),
    signature: {
      hash: Binary(Buffer.from("20261a09eb39d162161f0fd0804d2cac3b480f70", "hex"), 0),
      keyId: Long("7154370897485234178")
    }
  },
  operationTime: Timestamp({ t: 1675683048, i: 1 })
}
```

