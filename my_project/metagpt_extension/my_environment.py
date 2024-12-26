from metagpt.environment import Environment

class MyEnvironment(Environment):
    def __init__(self, context=None):
        super().__init__(context=context)
        # Could store specialized logic or memory references

from .my_memory_manager import MemoryManager

if not hasattr(MyEnvironment, 'memory_manager'):
    MyEnvironment.memory_manager = MemoryManager("./memory_store.json")

original_run = MyEnvironment.run
async def myenv_run(self, max_steps=1):
    steps = 0
    while not self.is_idle and steps<max_steps:
        await self.run_once()
        for msg in self.history[-5:]:
            self.memory_manager.add_entry(role_name=str(msg.role), content=msg.content)
        steps+=1

MyEnvironment.run = myenv_run
