"""
conftest.py for shared pytest config or fixtures
"""
import pytest

@pytest.fixture(scope="session")
def test_config_path():
    return "config/settings.yaml"
