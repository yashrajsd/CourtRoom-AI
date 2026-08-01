from langchain_core.messages import (HumanMessage, AIMessage, SystemMessage)

from app.prompts.loader import PromptLoader
from app.agents.base import BaseAgent
from app.state.court_state import CourtState

class LawyerAgent(BaseAgent):
    """
    Agent that acts as a lawyer.
    """

    def __init__(self,llm):
        super().__init__(llm)

        self.system_prompt = PromptLoader.load("lawyer")

    async def invoke(self, state: CourtState) -> dict:
        messages = [
            SystemMessage(content=self.system_prompt),
            *state["conversation"]
        ]

        try:
            response = await self._llm.ainvoke(messages)
        except Exception as e:
            raise RuntimeError(f"LawyerAgent failed to invoke LLM: {e}") from e
  
        return {
            "conversation": [response[0].text]
        }