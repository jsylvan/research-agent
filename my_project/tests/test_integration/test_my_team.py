import pytest
import asyncio
from metagpt_extension.my_team import MyTeam
from metagpt.environment import Message

@pytest.mark.asyncio
async def test_my_team_integration(test_config_path):
    t = MyTeam(config_path=test_config_path)
    t.env.publish_message(Message(content="Integration test synergy."))
    await t.env.run(max_steps=2)
    assert len(t.env.history) > 0
