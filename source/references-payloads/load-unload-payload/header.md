A [Payload](https://openusd.org/release/glossary.html#usdglossary-payload) is a composition arc that you can choose not to load. An unloaded prim stays on the Stage with its own opinions, but nothing from its Payload is composed, so its Payload's descendants are not on the Stage. This lets you see the full hierarchy of a large scene and load only the heavy parts you need. Learn more about [loading and unloading Payloads](https://openusd.org/release/api/class_usd_stage.html#Usd_workingSetManagement). To author a Payload in the first place, see [Add a Payload](add-payload).

```{note}
Load state belongs to the Stage, not to its layers. Loading or unloading a Payload does not author anything, so it is not saved with the Stage. Stages load all Payloads by default; open a Stage with `Usd.Stage.LoadNone` to start with nothing loaded.
```
