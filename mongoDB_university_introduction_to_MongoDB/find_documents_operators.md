```
db.sales.find(
 { "items.price": { $gt: 200}}
)
```

```
db.sales.find(
 { "items.price": { $lt: 25}}
)
```

```
db.sales.find(
 { "items.quantity": { $gte: 10}}
)
```

```
db.sales.find(
 { "customer.age": { $lte: 45 } }
)
```
