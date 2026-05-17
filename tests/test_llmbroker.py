from llmbroker import __version__
from llmbroker.main import llmbroker
from click.testing import CliRunner


def test_version():
    assert __version__


def test_version_option():
    runner = CliRunner()
    result = runner.invoke(llmbroker, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.output
