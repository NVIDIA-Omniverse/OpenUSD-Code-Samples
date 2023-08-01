You can set the `metersPerUnit` metadata on the stage using `UsdGeom.SetStageMetersPerUnit`. Convenience shortcuts for units are scoped in `UsdGeom.LinearUnits` (e.g. `UsdGeom.LinearUnits.meters` is `1.0 metersPerUnit`)

```{note}
Fallback stage linear units are centimeters (0.01).
```

```{warning}
Existing objects will not be automatically scaled to adapt to the stage linear units. Learn more about [stage linear units](https://graphics.pixar.com/usd/release/api/group___usd_geom_linear_units__group.html).
```
    

