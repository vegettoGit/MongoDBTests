#### Solution

```
db.sales.countDocuments(
   {}
)
```

```
db.sales.countDocuments(
   { storeLocation: "Denver", couponUsed: true }
)
```

```
db.sales.countDocuments(
   { items: { $elemMatch: { name: "laptop", price: { $lt: 600 } } } } 
)
```
