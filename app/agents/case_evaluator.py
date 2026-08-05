from app.agents.structured import StructuredAgent
from app.prompts.loader import PromptLoader
from app.schemas.evaluation import EvaluationResultSchema
from app.state.court_state import CourtState


class CaseEvaluatorAgent(StructuredAgent):
    """
    Decides whether the lawyer should continue questioning
    or whether the case can move to the opponent.
    """

    def __init__(self, llm_service):
        super().__init__(llm_service)

        self._system_prompt = PromptLoader.load(
            "case_evaluator"
        )

    @property
    def system_prompt(self) -> str:
        return self._system_prompt

    @property
    def output_schema(self):
        return EvaluationResultSchema

    def process_result(
        self,
        result: EvaluationResultSchema,
        state: CourtState,
    ) -> dict:

        metadata = {
            **state["metadata"],
            "next_step": result.next_step,
        }

        return {
            "metadata": metadata
        }