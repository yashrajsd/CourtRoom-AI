from langgraph.graph import StateGraph,START,END

from app.agents.factory import AgentContainer
from app.state.court_state import CourtState
from app.graph.router import case_router

class CourtGraph:

    @staticmethod
    def build(agents: AgentContainer):
        builder = StateGraph(CourtState)

        builder.add_node("lawyer",agents.lawyer.invoke)
        builder.add_node("opponent",agents.opponent.invoke)
        builder.add_node("case_evaluator",agents.case_evaluator.invoke)

        builder.add_edge(START,"lawyer")
        builder.add_edge("lawyer","case_evaluator")
        
        builder.add_conditional_edges(
            "case_evaluator",
            case_router,
            {
                "lawyer":"lawyer",
                "opponent": "opponent"
            }
        )

        builder.add_edge("opponent",END)

        return builder.compile()