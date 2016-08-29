# -*- coding: utf-8 -*-

import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if pytest.config.getoption('--error-for-skips'):
        if rep.skipped and call.excinfo.errisinstance(pytest.skip.Exception):
            rep.outcome = 'failed'
            r = call.excinfo._getreprcrash()
            rep.longrepr = 'Forbidden skipped test - {message}'.format(message=r.message)


def pytest_addoption(parser):
    parser.addoption(
        '--error-for-skips',
        action='store_true',
        default=False,
        help='Treat skipped tests as errors'
    )
