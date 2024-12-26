import pytest
from metagpt_extension.my_engineer import MyEngineer

@pytest.mark.asyncio
async def test_my_engineer_implement_code(test_config_path):
    eng = MyEngineer(config_path=test_config_path)
    arch = {"content": "Proposed design..."}
    code = await eng.implement_code(arch)
    assert "content" in code
