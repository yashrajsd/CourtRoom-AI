from typing import TypedDict
from typing import Annotated
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from app.core.enums import NextStep

class Session(TypedDict):
    session_id: str
    user_id: str

class Case(TypedDict):
    title: str
    description: str
    category: str

class Evidence(TypedDict):
    description: str
    source: str
    confidence: float

class MetaData(TypedDict):
    current_agent: str
    is_completed: bool
    next_step: NextStep

class Verdict(TypedDict):
    decision: str | None
    confidence: float | None
    reasoning: str | None

class CourtState(TypedDict):

    """
    Shared state for a single courtroom hearing.
    """

    session: Session
    case: Case
    conversation: Annotated[list[BaseMessage], add_messages]
    evidence: list[Evidence]
    findings: list[str]
    verdict: Verdict
    metadata: MetaData

