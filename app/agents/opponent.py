from app.agents.base import BaseAgent
from app.state.court_state import CourtState
from app.prompts.loader import PromptLoader
from app.utils.message_builder import MessageBuilder

class OpponentAgent(BaseAgent):
    """
    Represents the opposing counsel.

    Generates the strongest possible counterarguments
    using the information currently available.
    """

    def __init__(self, llm_service):
        super().__init__(llm_service)
        self.system_prompt = PromptLoader.load("opponent")

    async def invoke(self,state: CourtState)->dict:

        messages = MessageBuilder.build(
            self.system_prompt,
            state["conversation"]
        )

        response = await self._llm_service.chat(messages)

        metadata = {
            **state["metadata"],
            "current_agent": "opponent",
        }

        return {"metadata": metadata, "conversation": [response]} 