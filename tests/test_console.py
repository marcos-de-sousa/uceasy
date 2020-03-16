import click.testing
import pytest

from uceasy import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(runner):
    result = runner.invoke(console.cli)
    assert result.exit_code == 0