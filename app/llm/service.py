from langchain_core.messages import AIMessage, BaseMessage
from langchain_core.language_models.chat_models import BaseChatModel
from typing import Type
from pydantic import BaseModel


class LLMService:
    """
    Wrapper around LangChain chat models

    Responsible for:
    - Invoking the LLM
    - Centralising error handling
    - Logging (TODO)
    - Toke usage tracking (TODO)
    - Retries (TODO)
    """

    def __init__(self, llm: BaseChatModel):
        self._llm = llm

    async def chat(
            self,
            messages: list[BaseMessage],
    )->AIMessage:
        try:
            response = await self._llm.ainvoke(messages)
            return response
        except Exception as e:
            raise RuntimeError(f"LLMService failed to invoke LLM: {e}") from e


    async def structured_chat(
            self,
            messages: list[BaseMessage],
            schema: Type[BaseModel]
    ):
        """
        Incoke the LLM and return a validated Pydantic model.
        """

        structured_llm = self._llm.with_structured_output(schema)

        return await structured_llm.ainvoke(messages)