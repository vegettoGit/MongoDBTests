#### Solution

```
db.sales.find(
   {}
).sort(
   { saleDate: 1 }
)
```

```
db.sales.find(
   { purchaseMethod: "Online", couponUsed: true}
).sort(
   { saleDate: -1 }
)
```

```
db.sales.find(
   { "items.name": { $in: ["laptop", "backpack", "printer paper"] }, "storeLocation": "London", }
).sort(
   { saleDate: -1, }
).limit(3)
```
