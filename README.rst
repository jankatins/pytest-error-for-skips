pytest-error-for-skips
======================

.. image:: https://travis-ci.org/janschulz/pytest-error-for-skips.svg?branch=master
    :target: https://travis-ci.org/janschulz/pytest-error-for-skips
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/janschulz/pytest-error-for-skips?branch=master
    :target: https://ci.appveyor.com/project/janschulz/pytest-error-for-skips/branch/master
    :alt: See Build Status on AppVeyor

.. image:: https://readthedocs.org/projects/pytest-plugin-to-treat-skipped-tests-as-errors/badge/?version=latest
	:target: http://pytest-plugin-to-treat-skipped-tests-as-errors.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. image:: https://badge.fury.io/py/pytest-error-for-skips.svg
    :target: https://badge.fury.io/py/pytest-error-for-skips
    :alt: PyPI Status

Pytest plugin to treat skipped tests a test failures.

This is nice if you want to ensure that your CI tests really run all tests and
don't skip tests because of missing dependencies.


Usage
-----

Simply execute your tests via ``py.test --error-for-skips ...`` and all skipped
tests become test failures.


Requirements
------------

* pytest


Installation
------------

You can install "pytest-error-for-skips" via `pip`_ from `PyPI`_::

    $ pip install pytest-error-for-skips


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

Simplest setup:
```bash
git clone https://github.com/jankatins/pytest-error-for-skips.git
cd pytest-error-for-skips
(mkdir env && cd env && python -m venv .)
source env/bin/acticate
python -m pip install -e .
pytest
```

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-error-for-skips" is
free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed
description.


----

This `Pytest`_ plugin was generated with `Cookiecutter`_ along with
`@hackebrot`_'s `Cookiecutter-pytest-plugin`_ template.


.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/janschulz/pytest-error-for-skips/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
