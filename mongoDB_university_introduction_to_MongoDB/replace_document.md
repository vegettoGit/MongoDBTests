```
db.birds.find(
 { common_name: "Northern Cardinal" }
)
```

### Returned result

```
[
  {
    _id: ObjectId("6286809e2f3fa87b7d86dccd"),
    common_name: 'Northern Cardinal',
    scientific_name: 'Cardinalis cardinalis',
    wingspan_cm: 25.32,
    habitat: 'woodlands',
    diet: [ 'grain', 'seeds', 'fruit' ],
    last_seen: ISODate("2022-05-19T20:20:44.083Z")
  }
]
```

```
db.birds.replaceOne(
 { _id: ObjectId("6286809e2f3fa87b7d86dccd") },
 {
   common_name: "Morning Dove",
   scientific_name: "Zenaida macroura",
   wingspan_cm: 37.23,
   habitat: ["urban areas", "farms", "grassland"],
   diet: ["seeds"],
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
