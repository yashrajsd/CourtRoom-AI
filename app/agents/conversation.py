from abc import  abstractmethod
from app.agents.base import BaseAgent
from app.state.court_state import CourtState
from app.utils.message_builder import MessageBuilder

class ConversationAgent(BaseAgent):
    """
    Base class for agents that communicate through natural language

    handles
    - Building the prompt
    - calling the LLM
    - Updating metadata
    """

    def __init__(self,llm_service):
        super().__init__(llm_service)

    @property
    @abstractmethod
    def system_prompt(self)->str:
        """
        Each conversational agent must provide its system prompt
        """

    @property
    @abstractmethod
    def agent_name(self)->str:
        """
        used to update metadata
        """

    async def invoke(self,state:CourtState)->dict:

        messages = MessageBuilder.build(
            self.system_prompt,
            state['conversation']
        )

        response = await self._llm_service.chat(messages)

        metadata = {
            **state['metadata'],
            "current_agent": self.agent_name,
        }

        return {
            "conversation": [response],
            "metadata": metadata,
        }
