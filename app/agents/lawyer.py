from langchain_core.messages import (HumanMessage, AIMessage, SystemMessage)

from app.agents.conversation import ConversationAgent
from app.prompts.loader import PromptLoader
from app.agents.base import BaseAgent
from app.state.court_state import CourtState
from app.utils.message_builder import MessageBuilder

class LawyerAgent(ConversationAgent):
    """
    Agent that acts as a lawyer.
    """

    def __init__(self,llm_service):
        super().__init__(llm_service)
        self._system_prompt = PromptLoader.load("lawyer")

    @property
    def system_prompt(self)->str:
        return self._system_prompt

    @property
    def agent_name(self)->str:
        return "lawyer"