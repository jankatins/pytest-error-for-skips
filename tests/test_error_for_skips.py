# -*- coding: utf-8 -*-


def test_skipped_to_failure(testdir):
    """Make sure that pytest accepts our fixture."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        import pytest
        @pytest.mark.skip(reason="dependencies not installed")
        def test_sth():
            assert False
    """)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--error-for-skips',
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_sth ERROR',
        'Forbidden skipped test - Skipped: dependencies not installed'
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 1

def test_skipped_still_works(testdir):
    """Make sure that pytest accepts our fixture."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        import pytest
        @pytest.mark.skip(reason="dependencies not installed")
        def test_sth():
            assert False
    """)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_sth SKIPPED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_help_message(testdir):
    result = testdir.runpytest(
        '--help',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*--error-for-skips*Treat skipped tests as errors*',
    ])
