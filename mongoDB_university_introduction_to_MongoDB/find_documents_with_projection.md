#### Solution

```
db.sales.find(
   { storeLocation: "Denver", }, 
   { storeLocation: 1, saleDate: 1, purchaseMethod: 1, }
)
```

```
db.sales.find(
   { "customer.age": { $lt: 30 }, "customer.satisfaction": { $gt: 3 }, }, 
   { "customer.satisfaction": 1, "customer.age": 1, "storeLocation": 1, "saleDate": 1, "_id": 0, }
)
```

```
db.sales.find(
   { storeLocation: { $in: ["Seattle", "New York"] }, }, 
   { couponUsed: 0, purchaseMethod: 0, customer: 0, }
)
```
