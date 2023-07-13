.. meta::
    :description: Universal Scene Description (USD) Python code snippets for getting the child of a Prim.
    :keywords: USD, Python, snippet, prim, child, children

==================================
Get the Child of a Prim
==================================

An example of hierarchy and traversal within a smaller scope is getting the child of a prim. These snippets show how to get a single child by name or how to iterate through all of the children of a prim.

USD API
--------------
If you know the name of the child prim, you can use :code:`Usd.Prim.GetChild()`. This returns an invalid prim if the child doesn't exist. You can :doc:`check if the returned prim exists <../prims/check-prim-exists>`.

.. code-block:: python

    from pxr import Usd

    child_prim: Usd.Prim = parent_prim.GetChild("MyChildPrim")    

Another option is to iterate through all of the prim's children to operate on all the children or query them to find the child you are looking for.

.. code-block:: python
    
    from pxr import Usd, UsdGeom

    def get_first_child_mesh(parent_prim: Usd.Prim) -> Usd.Prim:
        # Iterates only active, loaded, defined, non-abstract children
        for child_prim in parent_prim.GetChildren():
            if child_prim.IsA(UsdGeom.Mesh):
                return child_prim
    
    def print_all_children_names(parent_prim: Usd.Prim):
        # Iterates over all children
        for child_prim in parent_prim.GetAllChildren():
            print(child_prim.GetName())
        