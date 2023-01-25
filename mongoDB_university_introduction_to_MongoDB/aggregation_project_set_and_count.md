#### Solution 1

```
db.sightings.aggregate([
  {
    $project: {
        _id: 0,
        species_common: 1,
        date: 1
    }
  }
])
```

### Returned result
```
[
  {
    species_common: 'Eastern Bluebird',
    date: ISODate("2022-01-18T21:09:00.000Z")
  },
  {
    species_common: 'Eastern Bluebird',
    date: ISODate("2022-01-18T18:22:20.000Z")
  },
  {
    species_common: 'Eastern Bluebird',
    date: ISODate("2022-01-18T18:24:00.000Z")
  },
  {
    species_common: 'Eastern Bluebird',
    date: ISODate("2022-01-17T18:24:00.000Z")
  },
  {
    species_common: 'Northern Cardinal',
    date: ISODate("2022-01-18T05:30:40.000Z")
  },
  {
    species_common: 'Eastern Bluebird',
    date: ISODate("2022-01-18T23:55:40.000Z")
  }
]
```

#### Solution 2

```
db.birds.aggregate([
  {
    $set: {
      'class': 'bird'
    }
  }
])
```

### Returned result
```
[
  {
    _id: ObjectId("626845c4613e55b82d7065d5"),
    common_name: 'Sanderling',
    scientific_name: 'Calidris alba',
    wingspan_cm: 43.18,
    habitat: 'wetlands',
    diet: [ 'crustaceans', 'oceanic invertebrates' ],
    last_seen: ISODate("2022-05-19T20:20:44.083Z"),
    class: 'bird'
  },
  {
    _id: ObjectId("626844cc613e55b82d7065d3"),
    common_name: 'Bufflehead',
    scientific_name: 'Bucephala albeola',
    wingspan_cm: 53.3,
    habitat: 'wetlands',
    diet: [ 'snails', 'crustaceans', 'water plants' ],
    last_seen: ISODate("2022-05-19T20:20:44.083Z"),
    class: 'bird'
  },
  {
    _id: ObjectId("62684641613e55b82d7065d6"),
    common_name: 'Rock Pigeon',
    scientific_name: 'Columba livia',
    wingspan_cm: 71.12,
    habitat: [ 'urban parks', 'farmland' ],
    diet: [ 'grass', 'grain', 'fruit', 'weeds', 'vegetables' ],
    last_seen: ISODate("2022-05-19T20:20:44.083Z"),
    class: 'bird'
  },
  {
    _id: ObjectId("6268413c613e55b82d7065d2"),
    common_name: 'Canada Goose',
    scientific_name: 'Branta canadensis',
    wingspan_cm: 152.4,
    habitat: 'wetlands',
    diet: [ 'grass', 'algae' ],
    last_seen: ISODate("2022-05-19T20:20:44.083Z"),
    class: 'bird'
  },
  {
    _id: ObjectId("6286a5612f3fa87b7d86dcd2"),
    common_name: 'Grackle',
    scientific_name: 'Quiscalus quiscula',
    wingspan_cm: 28.04,
    habitat: 'pine trees',
    diet: [ 'insects', 'minnows', 'eggs' ],
    sightings_count: 7,
    last_seen: ISODate("2022-05-19T20:20:44.083Z"),
    class: 'bird'
  },
  {
    _id: ObjectId("6268471e613e55b82d7065d7"),
    common_name: 'Great Horned Owl',
    scientific_name: 'Bubo virginianus',
    wingspan_cm: 111.76,
    habitat: [ 'grasslands', 'farmland', 'tall forest' ],
    diet: [ 'mice', 'small mammals', 'rabbits', 'shrews' ],
    last_seen: ISODate("2022-05-19T20:20:44.083Z"),
    class: 'bird'
  },
  {
    _id: ObjectId("62cddf53c1d62bc45439bebf"),
    common_name: 'Grey Catbird',
    scientific_name: 'Dumetella carolinensis',
    wingspan_cm: 26.04,
    habitat: [ 'vegetation', 'Scrublands', 'woodlands' ],
    diet: [ 'fruit', 'berries', 'worms' ],
    sightings_count: 3,
    class: 'bird'
  },
  {
    _id: ObjectId("62684c8c613e55b82d7065d8"),
    common_name: 'Purple Martin',
    scientific_name: 'Progne Subis',
    wingspan_cm: 45.72,
    habitat: 'field',
    diet: [ 'insects' ],
    last_seen: ISODate("2022-05-19T20:20:44.083Z"),
    class: 'bird'
  },
  {
    _id: ObjectId("62684551613e55b82d7065d4"),
    common_name: 'Great Blue Heron',
    scientific_name: 'Ardea herodias',
    wingspan_cm: 182.88,
    habitat: 'wetlands',
    diet: [ 'snails', 'crustaceans', 'fish', 'frogs', 'snakes' ],
    last_seen: ISODate("2022-05-19T20:20:44.083Z"),
    class: 'bird'
  },
  {
    _id: ObjectId("628682d92f3fa87b7d86dcce"),
    common_name: 'Blue Jay',
    scientific_name: 'Cyanocitta cristata',
    wingspan_cm: 34.17,
    habitat: 'forests',
    diet: [ 'vegetables', 'nuts', 'grains' ],
    sightings_count: 4,
    last_seen: ISODate("2022-05-19T20:20:44.083Z"),
    class: 'bird'
  },
  {
    _id: ObjectId("6286809e2f3fa87b7d86dccd"),
    common_name: 'Northern Cardinal',
    scientific_name: 'Cardinalis cardinalis',
    wingspan_cm: 25.32,
    habitat: 'woodlands',
    diet: [ 'grain', 'seeds', 'fruit' ],
    last_seen: ISODate("2022-05-19T20:20:44.083Z"),
    class: 'bird'
  },
  {
    _id: ObjectId("62684d24613e55b82d7065d9"),
    common_name: 'Palm Warbler',
    scientific_name: 'Setaphaga palmarum',
    wingspan_cm: 20.32,
    habitat: 'field',
    diet: [ 'insects', 'seeds', 'berries' ],
    last_seen: ISODate("2022-05-19T20:20:44.083Z"),
    class: 'bird'
  }
]
```

#### Solution 3

```
db.sightings.aggregate([
{
  $match: {
    date: {
      $gt: ISODate('2022-01-01T00:00:00.000Z'),
      $lt: ISODate('2023-01-01T00:00:00.000Z')
    },
    species_common: 'Eastern Bluebird'
  }
}, {
  $count: 'bluebird_sightings_2022'
}
])
```

### Returned result
```
[ { bluebird_sightings_2022: 5 } ]
```
