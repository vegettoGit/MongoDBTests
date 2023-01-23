```
db.birds.findAndModify(
  {
    query: { common_name: "Blue Jay" },
    update: { $inc: { sightings_count: 1 }},
    new: true,
  }
)
```

### Returned result

```
{
  _id: ObjectId("628682d92f3fa87b7d86dcce"),
  common_name: 'Blue Jay',
  scientific_name: 'Cyanocitta cristata',
  wingspan_cm: 34.17,
  habitat: 'forests',
  diet: [ 'vegetables', 'nuts', 'grains' ],
  sightings_count: 5,
  last_seen: ISODate("2022-05-19T20:20:44.083Z")
}
```

