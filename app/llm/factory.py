from app.llm.providers import LLMProvider
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.language_models.chat_models import BaseChatModel
from app.core.settings import settings

class LLMFactory:
    """
    Factory responsible for creating configured LLM Instances
    """

    @staticmethod
    def create(provider: LLMProvider = LLMProvider.GEMINI)->BaseChatModel:
        if provider == LLMProvider.GEMINI:
            return ChatGoogleGenerativeAI(
                model=settings.GEMINI_MODEL,
                google_api_key=settings.GOOGLE_API_KEY,
                temperature=settings.LLM_TEMPERATURE
            )
        
        raise NotImplementedError