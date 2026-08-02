from dataclasses import dataclass

from app.agents.lawyer import LawyerAgent
from app.agents.case_evaluator import CaseEvaluatorAgent
from app.agents.opponent import OpponentAgent
from app.llm.service import LLMService


@dataclass(slots=True)
class AgentContainer:
    """
    Holds all agents used by the LangGraph.
    """

    lawyer: LawyerAgent
    case_evaluator: CaseEvaluatorAgent
    opponent: OpponentAgent


class AgentFactory:
    """
    Responsible for creating all AI agents.
    """

    @staticmethod
    def create(llm_service: LLMService) -> AgentContainer:
        return AgentContainer(
            lawyer=LawyerAgent(llm_service),
            case_evaluator=CaseEvaluatorAgent(llm_service),
            opponent=OpponentAgent(llm_service),
        )