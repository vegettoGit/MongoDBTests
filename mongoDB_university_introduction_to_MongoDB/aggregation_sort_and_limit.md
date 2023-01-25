#### Solution

```
db.sightings.aggregate([
  {
    $sort: {
        'location.latitude': -1
    }
  }, {
    $limit: 4
  }
])
```

### Returned result
```
[
  {
    _id: ObjectId("62cf8e9fbb9cdbee29caab02"),
    species_common: 'Eastern Bluebird',
    species_scientific: 'Sialia sialis',
    date: ISODate("2022-01-18T18:22:20.000Z"),
    location: { type: 'Point', coordinates: [ 40, -74 ] }
  },
  {
    _id: ObjectId("62cf2f0acfe5bbb25ee815fb"),
    species_common: 'Eastern Bluebird',
    species_scientific: 'Sialia sialis',
    date: ISODate("2022-01-17T18:24:00.000Z"),
    location: { type: 'Point', coordinates: [ 41, -74 ] }
  },
  {
    _id: ObjectId("62cf8ebfbb9cdbee29caab04"),
    species_common: 'Eastern Bluebird',
    species_scientific: 'Sialia sialis',
    date: ISODate("2022-01-18T21:09:00.000Z"),
    location: { type: 'Point', coordinates: [ 40, -74 ] }
  },
  {
    _id: ObjectId("62cf32bdcfe5bbb25ee815fc"),
    species_common: 'Eastern Bluebird',
    species_scientific: 'Sialia sialis',
    date: ISODate("2022-01-18T18:24:00.000Z"),
    location: { type: 'Point', coordinates: [ 40, -73 ] }
  }
]
```

