See [USD: Visibility](https://openusd.org/release/glossary.html#usdglossary-visibility). You can show or hide a prim by setting the `visibility` attribute to either `inherited` or `invisible`.

If the value is set to `inherited`, the prim is visible only if none of its imageable ancestors has a visibility value of `invisible`. Setting `inherited` on a prim does not override an invisible ancestor.
If the value is set to `invisible`, then the prim and all descendant prims will be invisible.

Reading the attribute alone does not account for ancestor visibility. See [Get the Visibility of a Prim](get-prim-visibility) to check the computed visibility with `UsdGeom.Imageable.ComputeVisibility()`.
