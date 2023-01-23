```
db.sales.find(
 { couponUsed: true,  purchaseMethod: "Online", "customer.age": { $lte: 25 } }
)
```

```
db.sales.find(
 {
   $or: [{ "items.name": "pens" }, { "items.tags": "writing" }],
 }
)
```

