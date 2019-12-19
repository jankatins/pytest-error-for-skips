pytest-error-for-skips
======================

[![See Build Status on Travis CI](https://travis-ci.org/jankatins/pytest-error-for-skips.svg?branch=master)](https://travis-ci.org/jankatins/pytest-error-for-skips)

[![See Build Status on AppVeyor](https://ci.appveyor.com/api/projects/status/github/jankatins/pytest-error-for-skips?branch=master)](https://ci.appveyor.com/project/jankatins/pytest-error-for-skips/branch/master)

[![Documentation Status](https://readthedocs.org/projects/pytest-plugin-to-treat-skipped-tests-as-errors/badge/?version=latest)](http://pytest-plugin-to-treat-skipped-tests-as-errors.readthedocs.io/en/latest/?badge=latest)

[![PyPI Status](https://badge.fury.io/py/pytest-error-for-skips.svg)](https://badge.fury.io/py/pytest-error-for-skips)

Pytest plugin to treat skipped tests a test failures.

This is nice if you want to ensure that your CI tests really run all
tests and don\'t skip tests because of missing dependencies.

Usage
-----

Simply execute your tests via `pytest --error-for-skips ...` and all
skipped tests become test failures.

Requirements
------------

-   pytest

Installation
------------

You can install \"pytest-error-for-skips\" via
[pip](https://pypi.python.org/pypi/pip/) from
[PyPI](https://pypi.python.org/pypi):

```bash
pip install pytest-error-for-skips
```

Contributing
------------

Contributions are very welcome. Tests can be run with
[tox](https://tox.readthedocs.io/en/latest/), please ensure the coverage
at least stays the same before you submit a pull request.

Simplest setup:

```bash
git clone <https://github.com/jankatins/pytest-error-for-skips.git
cd pytest-error-for-skips
(mkdir env && cd env && python -m venv> .) 
source env/bin/acticate
python -m pip install -e .
pytest
```

License
-------

Distributed under the terms of the
[MIT](http://opensource.org/licenses/MIT) license,
\"pytest-error-for-skips\" is free and open source software

Issues
------

If you encounter any problems, please [file an
issue](https://github.com/jankatins/pytest-error-for-skips/issues) along
with a detailed description.

------------------------------------------------------------------------

This [Pytest](https://github.com/pytest-dev/pytest) plugin was generated
with [Cookiecutter](https://github.com/audreyr/cookiecutter) along with
[\@hackebrot](https://github.com/hackebrot)\'s
[Cookiecutter-pytest-plugin](https://github.com/pytest-dev/cookiecutter-pytest-plugin)
template.
