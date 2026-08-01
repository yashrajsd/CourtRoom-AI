from typing import Literal
from pydantic import BaseModel, Field
from app.core.enums import NextStep

class EvaluationResultSchema(BaseModel):
    """
    Decision made by the CaseEvaluatorAgent.
    """

    next_step: NextStep = Field(
        description="Which agent should execute next."
    )

    reason: str = Field(
        description="Short explanation for the decision."
    )
