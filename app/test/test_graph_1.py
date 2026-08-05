import asyncio
from langchain_core.messages import HumanMessage
from app.agents.factory import AgentFactory
from app.graph.court_graph import CourtGraph
from app.llm.service import LLMService
from app.llm.factory import LLMFactory
from app.core.enums import NextStep

async def main():
    llm = LLMFactory.create()
    service = LLMService(llm)
    agents = AgentFactory.create(service)
    graph = CourtGraph.build(agents)

    state = {
                "session": {
            "session_id": "1",
            "user_id": "demo",
        },
        "case": {
            "title": "Salary Dispute",
            "description": "Employer refused salary",
            "category": "Employment",
        },
        "conversation": [
            HumanMessage(
                content="My employer fired me without notice and didn't pay my final salary."
            )
        ],
        "evidence": [],
        "findings": [],
        "verdict": {},
        "metadata": {
            "current_agent": "lawyer",
            "is_completed": False,
            "next_step": NextStep.LAWYER,
        },
    }

    result = await graph.ainvoke(state) 

    print(result)

if __name__ == "__main__":   
    asyncio.run(main())