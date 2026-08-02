from app.core.enums import NextStep
from app.state.court_state import CourtState

def case_router(state: CourtState)-> str:
    """
    Decide which node should execute next
    """

    return state["metadata"]["next_step"].value