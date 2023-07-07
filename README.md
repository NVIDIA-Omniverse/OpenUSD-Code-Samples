# OpenUSD-Code-Samples
Common code snippets for OpenUSD

- usd
- kit_commands
- omni_usd
- usdrt

## Getting Started

```console
git clone https://github.com/NVIDIA-Omniverse/OpenUSD-Code-Samples
cd OpenUSD-Code-Samples
poetry install
poetry run create-material-mesh
```

Install poetry at <https://python-poetry.org/>

# Ideas
## Google Collab so you can run in browser
https://github.com/NVIDIA-Omniverse/USD-Tutorials-And-Examples

# Repo Format

## Markdown YOLO
| Pros | Cons |
| -----|----- |
| It's just markdown | Hard to test? |
| Parsing code block isn't too hard | Hard to parse everything else. |
| Free rein | Free rein |
| | Hard to change the layout | 

## Formatted Code
| Pros | Cons |
| -----|----- |
| One file per flavor | Potentially fragile formatting |
| All code | Potential for ambiguous formatting errors |
| Fairly flexible for layout changes | Need to figure out how to parse C++ |


## Granular
| Pros | Cons |
| -----|----- |
| No parsing required | Lots of files |
| Most modular in case of layout changes | Need a diagram to show how it all fits together |

# Other Choices

## Markdown vs RST
### Markdown
- Everyone knows Markdown.
- MD can be included in our Sphinx RST. 
- We might run into translation issues for more advanced markup.

### RST
- RST plugs in directly into our Sphinx docs.
- If we do RST, there would be plenty of examples in the repo to learn RST.

## Function-wrapped vs Script-like
### Function-wrapped with Full Usage
```python
from pxr import Usd, UsdGeom, Gf

def compute_bbox_with_cache(cache: UsdGeom.BBoxCache, prim: Usd.Prim) -> Gf.Range3d:
    bound = cache.ComputeWorldBound(prim)
    bound_range = bound.ComputeAlignedBox()
    return bound_range

# Full Usage
stage = Usd.Stage.CreateNew(...)
...
stage.Export()
```

- Easily testable
- No ambiguity for variable types
- Verbose

### Script-like
```python
# Create the variant set and add your variants to it.
variants = ["red", "blue", "green"]
shading_varset = prim.GetVariantSets().AddVariantSet("shading")
for variant_name in variants:
    shading_varset.AddVariant(variant_name)

# Author opinions in for each variant. You could do this in the previous for loop too.
for variant_name in variants:
    # You must select a variant to author opinion for it.
    shading_varset.SetVariantSelection(variant_name)
    with shading_varset.GetVariantEditContext():
        # Specs authored within this context are authored just for the variant.
        ...

# Remember to set the variant you want selected once you're done authoring.
shading_varset.SetVariantSelection(variants[0])
```
- Less verbose
- More snippet-like
- Generally not runnable or testable
- Uses hard-coded literals or ambiguous or unscoped variables
