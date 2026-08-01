from  langchain_core.messages import (BaseMessage,SystemMessage)

class MessageBuilder:
    """
    Builds the message list sent to the LLM
    """

    @staticmethod
    def build(system_prompt:str,conversation:list[BaseMessage])-> list[BaseMessage]:
        return [SystemMessage(content=system_prompt),*conversation]