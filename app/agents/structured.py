from abc import abstractmethod
from typing import Type

from pydantic import BaseModel

from app.agents.base import BaseAgent
from app.state.court_state import CourtState
from app.utils.message_builder import MessageBuilder


class StructuredAgent(BaseAgent):
    """
    Base class for agents that return structured output.

    Handles:
    - Building messages
    - Calling structured_chat()
    - Returning validated schema
    """

    @property
    @abstractmethod
    def system_prompt(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def output_schema(self) -> Type[BaseModel]:
        raise NotImplementedError

    @abstractmethod
    def process_result(
        self,
        result:BaseModel,
        state:CourtState,
    )->dict:
        """
        Convert the structured output into langgraph state updates
        """

        return NotImplementedError

    async def invoke(self, state: CourtState) -> BaseModel:

        messages = MessageBuilder.build(
            self.system_prompt,
            state["conversation"],
        )

        result = await self._llm_service.structured_chat(
            messages=messages,
            schema=self.output_schema,
        )

        return self.process_result(
            result,
            state
        )