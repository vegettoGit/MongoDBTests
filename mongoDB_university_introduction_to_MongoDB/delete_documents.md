```
db.birds.deleteMany(
   { sightings_count: { $lte: 10 } }
)
```

### Returned result

```
{ acknowledged: true, deletedCount: 3 }
```

