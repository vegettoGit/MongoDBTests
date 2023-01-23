```
db.accounts.find(
 { products: "CurrencyService" }
)
```

```
db.transactions.find(
 {
    transactions: {
      $elemMatch: { amount: { $lte: 4500 }, transaction_code: "sell" },
    },
 }
)
```

