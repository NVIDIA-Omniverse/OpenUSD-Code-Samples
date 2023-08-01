Certain functions may return a `Usd.Property` object, but the Property may not exist due to an incorrect path or because of changes on the Stage. You can use [Usd.Object.IsValid()](https://openusd.org/release/api/class_usd_object.html#ac532c4b500b1a85ea22217f2c65a70ed) to check if the Property is valid or exists.

```{note}
Remember, that Properties consist of `Usd.Attribute` and `Usd.Relationship`. You can perform this check on both types of objects.
```
    