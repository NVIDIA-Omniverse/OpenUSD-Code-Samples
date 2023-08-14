# OpenUSD Code Samples
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![See the Code Samples](https://img.shields.io/badge/OpenUSD-Code_Samples-green
)](https://docs.omniverse.nvidia.com/dev-guide/latest/programmer_ref/usd.html)

This repository contains useful Universal Scene Description (OpenUSD) code samples in Python, C++, and USDA. If you want to browse the code samples to use them, you can see them fully rendered in the [OpenUSD Code Samples documentation](https://docs.omniverse.nvidia.com/dev-guide/latest/programmer_ref/usd.html) page.

## Configuration
This repository uses [Poetry](https://python-poetry.org/docs/) for dependency management. If you're new to Poetry, you don't need to know much more than the commands we use in the [build instructions](#How-to-Build). To make it easier when authoring code samples and contributing, we recommend installing:
1. Install any version of Python between versions 3.8-3.10 .
1. [Install Poetry](https://python-poetry.org/docs/#installation)

## How to Build
1. `poetry install`
1. `poetry run python build_docs.py`
1. In a web browser, open `sphinx/_build/index.html`

## Have an Idea for a New Code Sample?
Ideas for new code samples that could help other developers are always welcome. Please [create a new issue](https://github.com/NVIDIA-Omniverse/OpenUSD-Code-Samples/issues) requesting a new code sample and add the _new request_ label. Someone from the NVIDIA team or OpenUSD community will pick it up. If you can contribute it yourself, even better!

## Find a Typo or an Error?
Please let us know if you find any mistakes or non-working code samples. [File an issue](https://github.com/NVIDIA-Omniverse/OpenUSD-Code-Samples/issues) with a _bug_ label to let us know and so we can address it.

## Contributing
Contributions are welcome! If you would like to contribute, please read our [Contributing Guidelines](./CONTRIBUTING.md) to understand how to contribute. Also, check out the [Code Sample Guidelines](CODE-SAMPLE-GUIDELINES.md) to understand how code samples file and folders are structured in this repository and how to adhere to follow our code samples style.
