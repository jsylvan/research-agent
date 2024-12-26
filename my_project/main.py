import sys
from config.llm_config import LLMConfig

def main_main():
    config = LLMConfig()
    summ_cfg = config.get_model_config("summarization")
    adv_cfg = config.get_model_config("advanced_reasoning")

    print("Summarization model config:", summ_cfg)
    print("Advanced reasoning model config:", adv_cfg)

if __name__ == "__main__":
    main_main()

##############################
# Step 2 DEMO: SummarizeAgent & AdvancedAgent
##############################
from agents.summarize_agent import SummarizeAgent
from agents.advanced_agent import AdvancedAgent
from config.llm_config import LLMConfig

def step2_demo():
    print("\\n=== Step 2 Demo: SummarizeAgent & AdvancedAgent ===")
    cfg = LLMConfig()
    sum_agent = SummarizeAgent(cfg)
    adv_agent = AdvancedAgent(cfg)

    sample_text = "Large Language Models (LLMs) can generate text. Summaries are helpful."
    print("\\n[SummarizeAgent] Summarizing sample text:")
    summary = sum_agent.summarize_text(sample_text)
    print("Summary:", summary)

    sample_query = "Explain chain-of-thought for advanced math solutions."
    print("\\n[AdvancedAgent] Reasoning about complex query:")
    answer = adv_agent.reason_about(sample_query)
    print("Reasoned answer:", answer)

def original_main():
    main_main()

def main():
    print("\\n--- Original main() output from Step 1 ---")
    original_main()
    step2_demo()

main_main = main_main
main_main = None

if __name__ == "__main__":
    main()

##############################
# Step 3 DEMO: MyResearcher & MyTeam
##############################
import asyncio
from metagpt_extension.my_researcher import MyResearcher
from metagpt_extension.my_team import MyTeam

def step3_demo():
    print("\\n=== Step 3 Demo: Integrating with MetaGPT Researcher ===")

    async def demo_research():
        researcher = MyResearcher("config/settings.yaml", purpose="advanced_reasoning")
        output = await researcher.run_my_custom_research("Will quantum computing break encryption soon?")
        print("[MyResearcher] custom research:", output)

        team = MyTeam("config/settings.yaml")
        results = await team.run_project("Impacts of VR in Education")
        print("[MyTeam] results:", results)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(demo_research())

def extended_main():
    print("\\n--- Step 2 Demo output above ---")
    if 'step2_demo' in globals():
        pass
    step3_demo()

original_main2 = main
main = extended_main

if __name__ == "__main__":
    main()

##############################
# Step 4 DEMO: synergy with multiple roles
##############################
def step4_demo():
    print("\\n=== Step 4 Demo: synergy with multiple roles in MyTeam ===")
    import asyncio
    from metagpt_extension.my_team import MyTeam

    async def synergy_demo():
        team = MyTeam("config/settings.yaml")
        final_results = await team.run_project("Build a B2B SaaS with PaymentX")
        print("\\n[MyTeam synergy] final results:")
        for k,v in final_results.items():
            print(f"{k}: {v}")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(synergy_demo())

def synergy_main():
    if 'extended_main' in globals():
        extended_main()
    else:
        print("Skipping step 3 if not found.")
    step4_demo()

prev_main = main
main = synergy_main

if __name__ == "__main__":
    main()

##############################
# Step 5 DEMO: environment-based approach
##############################
def step5_demo():
    print("\\n=== Step 5 Demo: environment-based synergy with MyTeam ===")
    import asyncio
    from metagpt_extension.my_team import MyTeam

    async def environment_demo():
        team = MyTeam("config/settings.yaml")
        final_history = await team.run_project("Research VR in Education, propose quick architecture", n_rounds=4)
        print("\\n[MyTeam environment-based run] final environment history:")
        for i, msg in enumerate(final_history):
            print(f"Msg {i}: {msg}")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(environment_demo())

def environment_main():
    if 'synergy_main' in globals():
        synergy_main()
    else:
        print("Skipping step 4 if not found.")
    step5_demo()

previous_main2 = main
main = environment_main

if __name__ == "__main__":
    main()

##############################
# Step 6 DEMO: real chain-of-thought LLM usage
##############################
def step6_demo():
    print("\\n=== Step 6 Demo: real chain-of-thought approach in roles ===")
    import asyncio
    from metagpt_extension.my_team import MyTeam

    async def llm_demo():
        team = MyTeam("config/settings.yaml")
        final_msgs = await team.run_project("Develop an AI-based summary system", n_rounds=2)
        print("\\n[Step6 Demo] final environment messages:")
        for i,m in enumerate(final_msgs):
            print(f"{i}: {m}")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(llm_demo())

def llm_main():
    if 'environment_main' in globals():
        environment_main()
    step6_demo()

prev_main2 = main
main = llm_main

if __name__ == "__main__":
    main()

##############################
# Step 7 DEMO: Human-in-the-loop
##############################
def step7_demo():
    print("\\n=== Step 7 Demo: Human-in-the-loop ===")
    import asyncio
    from metagpt_extension.my_team import MyTeam
    from metagpt.environment import Message
    from metagpt.logs import logger

    async def human_demo():
        t = MyTeam("config/settings.yaml")
        t.add_human_in_the_loop()

        t.env.publish_message(Message(content="We want a VR product. Not sure about budget."))
        logger.info("[step7_demo] published user request.")
        t.env.publish_message(Message(content="NeedHumanInput: Please clarify budget?"))

        for round_idx in range(1,4):
            logger.info(f"--- step7 round {round_idx} ---")
            await t.env.run()
            if t.env.is_idle:
                break

        final_hist = [m.content for m in t.env.history]
        print("\\n** step7 final environment messages **")
        for i, c in enumerate(final_hist):
            print(f"{i}: {c}")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(human_demo())

def human_loop_main():
    if 'llm_main' in globals():
        llm_main()
    step7_demo()

prev_main3 = main
main = human_loop_main

if __name__ == "__main__":
    main()

##############################
# Step 8 DEMO: advanced memory usage
##############################
def step8_demo():
    print("\\n=== Step 8 Demo: MemoryManager usage ===")
    import asyncio
    from metagpt_extension.my_team import MyTeam
    from metagpt.environment import Message

    async def memory_demo():
        team = MyTeam("config/settings.yaml")
        team.env.publish_message(Message(content="Build an AR system, test memory logs."))

        await team.env.run(max_steps=2)
        mem_data = team.env.memory_manager.query_latest(limit=10)
        print("\\n** Memory manager last 10 entries **")
        for i, e in enumerate(mem_data):
            print(f'{i}: {e["role"]} => {e["content"]}')

        team.env.publish_message(Message(content="Another msg for memory."))
        await team.env.run(max_steps=2)
        mem_data2 = team.env.memory_manager.query_latest(limit=10)
        print("\\n** After more steps **")
        for i, e in enumerate(mem_data2):
            print(f'{i}: {e["role"]} => {e["content"]}')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(memory_demo())

def memory_main():
    if 'human_loop_main' in globals():
        human_loop_main()
    step8_demo()

older_main = main
main = memory_main

if __name__ == "__main__":
    main()
