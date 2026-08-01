from langgraph.graph import StateGraph, START, END

from app.agents.lawyer import LawyerAgent
from app.llm.factory import LLMFactory
from app.state.court_state import CourtState


def build_graph():
    llm = LLMFactory.create()

    lawyer = LawyerAgent(llm)

    builder = StateGraph(CourtState)

    builder.add_node("lawyer", lawyer.invoke)

    builder.add_edge(START, "lawyer")
    builder.add_edge("lawyer", END)

    return builder.compile()