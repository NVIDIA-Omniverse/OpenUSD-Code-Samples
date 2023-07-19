# OpenUSD-Code-Samples
Common code snippets for OpenUSD

- usd
- kit_commands
- omni_usd
- usdrt


# How to build
1. `pip install -r requirements.txt`
2. `python build.py`
3. In a web browser, open `sphinx/html/index.html`

# Samples Format

This image shows the file structure that contains two Code Samples for cameras. 

![Alt text](images/image.png)

Our Code Samples are stored in the source folder and organized by their categories in respective folders

In this example, we have two camera Code Samples. The paths to these two Code Samples folders are the following:

`source/cameras/create-orthographic-camera`
`source/cameras/create-perspective-camera`

**Within each Code Sample folder are the following files:**

| File(s) | Purpose |
| -----|----- |
| config.toml | Contains the title, metadata: description and SEO keywords |
| header.md | Hard to parse everything else. |
| Code Sample "flavor" file(s) | See below |
| Markdown file for each "flavor" | See below |


**Each Code Sample should have at least one "flavor":**

| Flavor Source File Name | Language and USD type |
| -----|----- |
| py_usd.py | Python using Pixar USD API |
| py_omni_usd.py | Python using omni.usd extension |
| py_kit_cmds.py | Python using Kit commands |
| cpp_usd.cpp | C++ using Pixar USD API |
| cpp_omni_usd.cpp | C++ using omni.usd extension |
| cpp_kit_cmds.cpp | C++ using Kit commands |
| usda.usda | USDA (text) file |

Each flavor can have more than one sample (variations). In this case we append _var(X) where X starts with 1 and increments for as many sample variations as needed.

Example: `py_usd.py`, `py_usd_var1.py`, `py_usd_var2.py `, etc...

**Markdown files:**

Every flavor that has a sample needs exactly one markdown file, no matter how many samples are included. They will have the same name as the code samples (excluding the variations suffix), but with the .md extension.

Example, if you have some `py_usd.py` samples you'll need a `py_usd.md` file. In the markdown file you'll need to use the `literalinclude` directive 

Example:
```
    **Convert to Numpy Array**

    To convert a VtArray to a Numpy Array, simply pass the VtArray object to `numpy.array` constructor.

    ``` {literalinclude} py_usd.py
    :language: py
    ```

    **Convert from Numpy Array** 

    To convert a Numpy Array to a VtArray, you can use `FromNumpy()` from the VtArray class you want to convert to.

    ``` {literalinclude} py_usd_var1.py
    :language: py
    ``` 
```

This example includes two samples, with a description for each one.

# Building the Samples

When all of your files are in place you should build and verify your samples are correctly setup by running the build script:

```
>python build.py
```

If there are no errors, you can then view it by loading the root index.html file, in the ``sphinx/_build folder``, in a browser. 

![Alt text](images/root_index_file.png)



There are two ways to do this. The first way: 
1) Select the ``index.html`` file
2) Right click and select ``Copy Path`` 
3) Paste the path into address bar of your web browser  
![Alt text](images/copy_path.png)

The second way:
1) select the ``index.html`` file so it's showing in a VS Code window
2) Press ``Alt-B`` and it will be launched in your default web browser.

And enjoy the majesty!

---




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
