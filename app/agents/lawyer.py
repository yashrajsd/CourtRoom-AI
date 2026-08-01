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

    async def invoke(self, state):
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(
                content="My landlord didn't return my security deposit."
            )
        ]
        response = await self._llm.ainvoke(messages)
        return {
            "response": response.content
        }