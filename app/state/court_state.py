from typing import Literal, TypedDict
from typing import Annotated
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class Session(TypedDict):
    session_id: str
    user_id: str

class Case(TypedDict):
    title: str
    description: str
    category: str

class MetaData(TypedDict):
    current_agent: str
    completed: bool

class Verdict(TypedDict):
    decision: str
    confidence: float
    reasoning: str

class CourtState(TypedDict):
    """
    Shared state for a single courtroom heraing

    Every LangGraph node recieves this state and returns
    only the fileds it wants to update
    """

    sessions: Session
    case: Case
    conversations: list
    evidence: list
    findings: list
    verdict: Verdict
    metadata: MetaData

