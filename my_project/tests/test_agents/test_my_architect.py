import pytest
from metagpt_extension.my_architect import MyArchitect

@pytest.mark.asyncio
async def test_my_architect_produce_architecture(test_config_path):
    arch = MyArchitect(config_path=test_config_path)
    result = await arch.produce_architecture("We want a microservice design")
    assert "content" in result or "architecture_design" in result
