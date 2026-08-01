from abc import ABC, abstractmethod
from typing import Any

class BaseAgent(ABC):
    """
    Base class for all AI agent in the courtroom system

    Every agents recieves:
    - An LLm instance
    - The current graph state

    Every agent returns
    - A dictionary containing ONLY the updates it wants 
    to make to the shared graph state 
    """

    def __init__(self,llm: any)->None:
        self._llm = llm

    @property
    def name(self)->str:
        return self.__class__.__name__
    
    @abstractmethod
    async def run(self,state:dict) ->dict:
        """
        Execute the agent.

        Parameters
        ----------
        state : 
            The current state of the graph.
        
        Returns
        ----------
        dict :
            State updates the merge into graph
        """

        pass
