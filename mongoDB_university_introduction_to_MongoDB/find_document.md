#### Solution

```
db.sales.find(
 { _id: ObjectId("5bd761dcae323e45a93ccff4")}
)
```

#### Returned result
```
[
  {
    _id: ObjectId("5bd761dcae323e45a93ccff4"),
    saleDate: ISODate("2014-08-18T10:42:13.935Z"),
    items: [
      {
        name: 'backpack',
        tags: [ 'school', 'travel', 'kids' ],
        price: Decimal128("187.16"),
        quantity: 2
      },
      {
        name: 'printer paper',
        tags: [ 'office', 'stationary' ],
        price: Decimal128("20.61"),
        quantity: 10
      },
      {
        name: 'notepad',
        tags: [ 'office', 'writing', 'school' ],
        price: Decimal128("23.75"),
        quantity: 5
      },
      {
        name: 'envelopes',
        tags: [ 'stationary', 'office', 'general' ],
        price: Decimal128("9.44"),
        quantity: 5
      }
    ],
    storeLocation: 'San Diego',
    customer: { gender: 'F', age: 59, email: 'la@cevam.tj', satisfaction: 4 },
    couponUsed: false,
    purchaseMethod: 'In store'
  }
]
```