from langchain_core.messages import (HumanMessage, AIMessage, SystemMessage)

from app.prompts.loader import PromptLoader
from app.agents.base import BaseAgent
from app.state.court_state import CourtState
from app.utils.message_builder import MessageBuilder

class LawyerAgent(BaseAgent):
    """
    Agent that acts as a lawyer.
    """

    def __init__(self,llm_service):
        super().__init__(llm_service)

        self.system_prompt = PromptLoader.load("lawyer")

    async def invoke(self, state: CourtState) -> dict:
        messages =  MessageBuilder.build(self.system_prompt,state["conversation"])

        try:
            """
            LLM will only ask for chat response no knowledge about LLM
            """
            response = await self._llm_service.chat(messages)
        except Exception as e:
            raise RuntimeError(f"LawyerAgent failed to invoke LLM: {e}") from e
  
        return {
            "conversation": [response]
        }