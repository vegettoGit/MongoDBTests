```
db.birds.find(
  { common_name: "Canada Goose" }
)
```

### Returned result

```
[
  {
    _id: ObjectId("6268413c613e55b82d7065d2"),
    common_name: 'Canada Goose',
    scientific_name: 'Branta canadensis',
    wingspan_cm: 152.4,
    habitat: 'wetlands',
    diet: [ 'grass', 'algae' ],
    last_seen: ISODate("2022-05-19T20:20:44.083Z")
  }
]
```

```
db.birds.updateOne(
  {
    common_name: "Canada Goose",
  },
  {
    $set: {
      tags: ["geese", "herbivore", "migration"],
    },
  }
)
```

### Returned result

```
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
```

### Let's find the updated document

```
db.birds.find(
  { common_name: "Canada Goose" }
)
```

### Returned result

```
[
  {
    _id: ObjectId("6268413c613e55b82d7065d2"),
    common_name: 'Canada Goose',
    scientific_name: 'Branta canadensis',
    wingspan_cm: 152.4,
    habitat: 'wetlands',
    diet: [ 'grass', 'algae' ],
    last_seen: ISODate("2022-05-19T20:20:44.083Z"),
    tags: [ 'geese', 'herbivore', 'migration' ]
  }
]
```

### Now let's add an element to an array field within a document

```
db.birds.updateOne(
  { _id: ObjectId("6268471e613e55b82d7065d7") },
  {
    $push: {
      diet: { $each: ["newts", "opossum", "skunks", "squirrels"] },
    },
  }
)
```

### Returned result

```
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
```

### Let's find the updated document

```
db.birds.find(
  { _id: ObjectId("6268471e613e55b82d7065d7") }
)
```

### Returned result

```
[
  {
    _id: ObjectId("6268471e613e55b82d7065d7"),
    common_name: 'Great Horned Owl',
    scientific_name: 'Bubo virginianus',
    wingspan_cm: 111.76,
    habitat: [ 'grasslands', 'farmland', 'tall forest' ],
    diet: [
      'mice',
      'small mammals',
      'rabbits',
      'shrews',
      'newts',
      'opossum',
      'skunks',
      'squirrels'
    ],
    last_seen: ISODate("2022-05-19T20:20:44.083Z")
  }
]
```

### Return, Update, and Add a Document

```
db.birds.updateOne(
  {
    common_name: "Robin Redbreast",
  },
  {
    $inc: {
      "sightings": 1,
    },
    $set: {
      last_updated: new Date(),
    },
  },
  {
    upsert: true,
  }
)
```

### Returned result

```
{
  acknowledged: true,
  insertedId: ObjectId("63ced834e65a092e32e3cc6c"),
  matchedCount: 0,
  modifiedCount: 0,
  upsertedCount: 1
}
```

### Let's find the updated document

```
db.birds.find(
  { common_name: "Robin Redbreast" }
)
```

### Returned result

```
[
  {
    _id: ObjectId("63ced834e65a092e32e3cc6c"),
    common_name: 'Robin Redbreast',
    last_updated: ISODate("2023-01-23T18:55:48.365Z"),
    sightings: 1
  }
]
```

