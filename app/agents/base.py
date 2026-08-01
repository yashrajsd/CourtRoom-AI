from abc import ABC, abstractmethod

from app.llm.service import LLMService
from app.state.court_state import CourtState

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

    def __init__(self,llm_service: LLMService)->None:
        self._llm_service = llm_service

    @property
    def name(self)->str:
        return self.__class__.__name__
    
    @abstractmethod
    async def invoke(self,state:CourtState) ->CourtState:
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

        raise NotImplementedError("Subclasses must implement the run method.")