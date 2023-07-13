
.. meta::
    :description: Universal Scene Description (USD) Python code snippets for getting the current Stage in Omniverse Kit and USDView.
    :keywords: USD, Python, snippet, omni.usd, stage, Omniverse Kit, USDView

=================================
Get the Current Stage
=================================

USD itself does not currently have a notion of a user session associated with a current stage. This is handled by higher-level facilities in USD applications such as :code:`usdviewApi` in USDView and :code:`omni.usd` in Omniverse Kit.

Kit (omni.usd)
--------------
.. code-block:: python

    import omni.usd

    stage = omni.usd.get_context().get_stage()

USDView
-------
.. code-block:: python

    stage = usdviewApi.stage
