"""
my_human_agent.py

A HumanAgent that listens for "NeedHumanInput" messages
and prompts user with input().
"""
import asyncio
from metagpt.roles.role import Role
from metagpt.logs import logger

class HumanAgent(Role):
    def __init__(self, name="HumanAgent", profile="Human-in-the-loop", goal="Provide feedback", constraints=""):
        super().__init__(name, profile, goal, constraints)
        self._watch(["NeedHumanInput"])

    async def _act(self):
        if not self.rc.todo:
            return None
        msg = self.rc.todo
        if "NeedHumanInput" in msg.name or "NeedHumanInput" in msg.content:
            logger.info("[HumanAgent] Prompting user for feedback...")
            user_feedback = input("**[HumanAgent]** Please provide clarifications: ")
            return f"User feedback: {user_feedback}"
        return None
