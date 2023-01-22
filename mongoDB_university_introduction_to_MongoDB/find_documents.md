#### Solution

```
db.sales.find(
 { storeLocation: { $in: ["London", "New York"] } }
)
```

#### Returned result
```
[
  {
    _id: ObjectId("5bd761dcae323e45a93ccfec"),
    saleDate: ISODate("2017-12-03T18:39:48.253Z"),
    items: [
      {
        name: 'backpack',
        tags: [ 'school', 'travel', 'kids' ],
        price: Decimal128("127.59"),
        quantity: 3
      },
      {
        name: 'notepad',
        tags: [ 'office', 'writing', 'school' ],
        price: Decimal128("17.6"),
        quantity: 4
      },
      {
        name: 'binder',
        tags: [ 'school', 'general', 'organization' ],
        price: Decimal128("18.67"),
        quantity: 2
      },
      {
        name: 'pens',
        tags: [ 'writing', 'office', 'school', 'stationary' ],
        price: Decimal128("60.56"),
        quantity: 3
      },
      {
        name: 'notepad',
        tags: [ 'office', 'writing', 'school' ],
        price: Decimal128("28.41"),
        quantity: 1
      },
      {
        name: 'envelopes',
        tags: [ 'stationary', 'office', 'general' ],
        price: Decimal128("15.28"),
        quantity: 7
      },
      {
        name: 'laptop',
        tags: [ 'electronics', 'school', 'office' ],
        price: Decimal128("1259.02"),
        quantity: 3
      }
    ],
    storeLocation: 'London',
    customer: { gender: 'M', age: 40, email: 'dotzu@ib.sh', satisfaction: 4 },
    couponUsed: false,
    purchaseMethod: 'In store'
  },
  {
    _id: ObjectId("5bd761dcae323e45a93ccfee"),
    saleDate: ISODate("2014-11-11T02:13:51.893Z"),
    items: [
      {
        name: 'laptop',
        tags: [ 'electronics', 'school', 'office' ],
        price: Decimal128("604.12"),
        quantity: 4
      },
      {
        name: 'binder',
        tags: [ 'school', 'general', 'organization' ],
        price: Decimal128("11.05"),
        quantity: 7
      },
      {
        name: 'binder',
        tags: [ 'school', 'general', 'organization' ],
        price: Decimal128("20.94"),
        quantity: 5
      },
      {
        name: 'backpack',
        tags: [ 'school', 'travel', 'kids' ],
        price: Decimal128("61.16"),
        quantity: 5
      },
      {
        name: 'notepad',
        tags: [ 'office', 'writing', 'school' ],
        price: Decimal128("29.81"),
        quantity: 3
      },
      {
        name: 'printer paper',
        tags: [ 'office', 'stationary' ],
        price: Decimal128("31.19"),
        quantity: 5
      },
      {
        name: 'pens',
        tags: [ 'writing', 'office', 'school', 'stationary' ],
        price: Decimal128("47.12"),
        quantity: 1
      },
      {
        name: 'notepad',
        tags: [ 'office', 'writing', 'school' ],
        price: Decimal128("36.71"),
        quantity: 2
      },
      {
        name: 'pens',
        tags: [ 'writing', 'office', 'school', 'stationary' ],
        price: Decimal128("69.28"),
        quantity: 3
      },
      {
        name: 'notepad',
        tags: [ 'office', 'writing', 'school' ],
        price: Decimal128("14.05"),
        quantity: 1
      }
    ],
    storeLocation: 'London',
    customer: { gender: 'F', age: 40, email: 'pan@cak.zm', satisfaction: 5 },
    couponUsed: false,
    purchaseMethod: 'In store'
  },
  (...)
]
```