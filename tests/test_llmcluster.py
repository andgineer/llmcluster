from llmcluster import __version__
from llmcluster.main import llmcluster
from click.testing import CliRunner


def test_version():
    assert __version__


def test_version_option():
    runner = CliRunner()
    result = runner.invoke(llmcluster, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.output
