"""
my_team.py
Now environment-based approach:
"""
import asyncio
from metagpt.team import Team
from metagpt.roles.project_manager import ProjectManager
from .my_researcher import MyResearcher
from .my_architect import MyArchitect
from .my_engineer import MyEngineer
from .my_reviewer import MyReviewer
from .my_environment import MyEnvironment
from metagpt.actions.add_requirement import UserRequirement
from metagpt.logs import logger

class MyTeam:
    def __init__(self, config_path="config/settings.yaml"):
        self.config_path = config_path
        self.env = MyEnvironment()
        self.team = Team(env=self.env)

        pm = ProjectManager()
        researcher = MyResearcher(config_path=self.config_path, purpose="summarization")
        architect = MyArchitect(config_path=self.config_path, purpose="advanced_reasoning")
        engineer = MyEngineer(config_path=self.config_path, purpose="advanced_reasoning")
        reviewer = MyReviewer(config_path=self.config_path, purpose="summarization")

        self.team.hire([pm, researcher, architect, engineer, reviewer])

    async def run_project(self, idea: str, n_rounds=3):
        self.env.publish_message(UserRequirement().create_message(idea))
        logger.info(f"Published user requirement: {idea}")

        for round_idx in range(1, n_rounds+1):
            logger.info(f"--- MyTeam Round {round_idx}/{n_rounds} ---")
            await self.env.run()
            if self.env.is_idle:
                logger.info("Environment idle. Ending early.")
                break
        return [m.content for m in self.env.history]
def add_human_in_the_loop(self):
    from .my_human_agent import HumanAgent
    self.team.hire([HumanAgent()])
