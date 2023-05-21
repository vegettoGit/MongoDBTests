### Commit a transaction

```
const session = db.getMongo().startSession()

session.startTransaction()

const account = session.getDatabase('bank').getCollection('accounts')

account.insertOne({
  account_id: "MDB454252264",
  account_holder: "Florence Taylor",
  account_type: "savings",
  balance: 100.0,
  transfers_complete: [],
  last_updated: new Date()
})
account.updateOne( { account_id: "MDB963134500" }, {$inc: { balance: -100.00 }})

session.commitTransaction()
```

### Cancel a transaction

```
var session = db.getMongo().startSession()

session.startTransaction()

var account = session.getDatabase('bank').getCollection('accounts')

account.updateOne( { account_id: "MDB740836066" }, {$inc: { balance: 100 }})

account.updateOne( { account_id: "MDB963134500" }, {$inc: { balance: -5 }})

session.abortTransaction()
```

