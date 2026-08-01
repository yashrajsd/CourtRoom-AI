import asyncio
from langchain_core.messages import HumanMessage
from app.graph.court_graph import build_graph

async def main():
    graph = build_graph()

    initial_state = {
        "session": {
            "session_id": "1",
            "user_id": "yash"
        },
        "case": {
            "title": "Deposit dispute",
            "description": "Landlord won't return deposit",
            "category": "Civil"
        },
        "conversation": [
            HumanMessage(
                content="My landlord isn't returning my deposit."
            )
        ],
        "evidence": [],
        "findings": [],
        "verdict": {
            "decision": None,
            "confidence": None,
            "reasoning": None,
        },
        "metadata": {
            "current_agent": "lawyer",
            "is_completed": False,
        },
    }

    result = await graph.ainvoke(initial_state)

    print(result)

if __name__ == "__main__":
    asyncio.run(main())