You can set the start and end frame of a stage with `Usd.Stage.SetStartTimeCode` and `Usd.Stage.SetEndTimeCode`. They author the `startTimeCode` and `endTimeCode` metadata, which tell applications the frame range to play back. Learn more about [time codes](https://openusd.org/release/glossary.html#usdglossary-timecode).

```{note}
If no range is authored, both values fall back to 0. Time codes are frames by default: `timeCodesPerSecond` falls back to 24.
```

```{warning}
The values are authored in the stage's current edit target, which must be the root layer or the session layer. Learn more about [Usd.Stage](https://openusd.org/release/api/class_usd_stage.html).
```
