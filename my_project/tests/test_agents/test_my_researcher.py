import pytest
from metagpt_extension.my_researcher import MyResearcher

@pytest.mark.asyncio
async def test_my_researcher_run_custom_research(test_config_path):
    r = MyResearcher(config_path=test_config_path)
    results = await r.run_custom_research("Test Topic")
    assert "summary" in results
