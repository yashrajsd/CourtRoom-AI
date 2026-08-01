
from app.prompts.loader import PromptLoader
from app.agents.base import BaseAgent
from app.schemas.evaluation import EvaluationResultSchema
from app.state.court_state import CourtState
from app.utils.message_builder import MessageBuilder


class CaseEvaluatorAgent(BaseAgent):
    """
    Decides whether the lawyer should continue questioning
    or whether the case can move to the opponent.
    """

    def __init__(self,llm_service):
        super().__init__(llm_service)

        self.system_prompt = PromptLoader.load("case_evaluator")

    async def invoke(self, state: CourtState) -> dict:
        messages = MessageBuilder.build(self.system_prompt,state["conversation"])

        response = await self._llm_service.structured_chat(messages=messages,schema=EvaluationResultSchema)

        metadata = {
            **state["metadata"],
            "next_step": response.decision
        }

        return{
            "metadata": metadata
        }