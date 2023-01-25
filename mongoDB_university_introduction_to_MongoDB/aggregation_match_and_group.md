#### Solution

```
db.sightings.aggregate([
  {
    $match: {
        species_common: 'Eastern Bluebird'
    }
  }, {
    $group: {
        _id: '$location.coordinates',
        number_of_sightings: {
            $count: {}
        }
    }
  }
])
```

### Returned result
```
[
  { _id: [ 40, -74 ], number_of_sightings: 3 },
  { _id: [ 40, -73 ], number_of_sightings: 1 },
  { _id: [ 41, -74 ], number_of_sightings: 1 }
]
```

