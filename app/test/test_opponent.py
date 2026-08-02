import asyncio

from langchain_core.messages import HumanMessage
from app.agents.opponent import OpponentAgent
from app.llm.factory import LLMFactory
from app.llm.service import LLMService

async def main():
    llm = LLMFactory.create()
    service = LLMService(llm)

    opponent = OpponentAgent(service)

    state = {
        "session": {
            "session_id": "1",
            "user_id": "yash",
        },
        "case": {
            "title": "Salary Dispute",
            "description": "Employer refused to pay salary",
            "category": "Employment",
        },
        "conversation": [
            HumanMessage(
                content="""
My employer terminated me
without notice and has not
paid my final salary.
"""
            )
        ],
        "evidence": [],
        "findings": [],
        "verdict": None,
        "metadata": {
            "current_agent": "lawyer",
            "is_completed": False,
            "next_step": "judge",
        },
    }

    result = await opponent.invoke(state)

    print(result["conversation"][-1].content)
    

if __name__ == "__main__":
    asyncio.run(main())