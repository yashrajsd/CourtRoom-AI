from app.agents.conversation import ConversationAgent
from app.prompts.loader import PromptLoader


class OpponentAgent(ConversationAgent):
    """
    Represents the opposing counsel.

    Generates the strongest possible counterarguments
    using the information currently available.
    """

    def __init__(self, llm_service):
        super().__init__(llm_service)
        self._system_prompt = PromptLoader.load("opponent")

    @property
    def system_prompt(self) -> str:
        return self._system_prompt

    @property
    def agent_name(self) -> str:
        return "opponent"