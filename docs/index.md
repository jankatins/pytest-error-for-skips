# Welcome to pytest-error-for-skips

Pytest plugin to treat skipped tests a test failures.

This is nice if you want to ensure that your CI tests really run all tests and
don't skip tests because of missing dependencies.


## Usage

Simply execute your tests via ``py.test --error-for-skips ...`` and all skipped
tests become test failures.


## Requirements

* pytest


## Installation

You can install `pytest-error-for-skips` via `pip` from
[PyPI](https://pypi.org/project/pytest-error-for-skips/):

```sh
pip install pytest-error-for-skips
```
