import asyncio

from app.agents.lawyer import LawyerAgent
from app.llm.factory import LLMFactory

async def main():
    llm = LLMFactory.create()

    lawyer = LawyerAgent(llm)

    state = {
        "session": {},
        "case": {},
        "conversation": [],
        "evidence": [],
        "findings": [],
        "verdict": {},
        "metadata": {},
    }

    reseponse = await lawyer.invoke(state)
    print(reseponse)

if __name__ == "__main__":
    asyncio.run(main())