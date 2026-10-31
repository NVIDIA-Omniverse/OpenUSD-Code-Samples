A prim's `visibility` attribute does not, by itself, tell you whether the prim is hidden by an ancestor. A value of `invisible` hides the prim and its descendants. A value of `inherited` allows visibility to be determined by its ancestors, so the prim can still be invisible.

Use [UsdGeom.Imageable.ComputeVisibility()](https://openusd.org/release/api/class_usd_geom_imageable.html#ac0bfa1554d9b57303c14f71d084c578d) to compute visibility through the hierarchy. The result is `invisible` if the prim or any imageable ancestor is invisible; otherwise, it is `inherited`. This checks USD's general visibility attribute. Purpose-specific visibility, camera framing, and occlusion can also affect whether a prim appears in a rendered image.

To change the visibility attribute, see [Show or Hide a Prim](show-hide-prim).
