It's best practice to set the `defaultPrim` metadata on a Stage if the Stage's root layer may be used as a Reference or Payload. Otherwise, consumers of your Stage are forced to provide a target prim when they create a Reference or Payload arc. Even though the `Usd.Stage.SetDefaultPrim()` accepts any `Usd.Prim`, the default prim must be a top-level prim on the Stage.

