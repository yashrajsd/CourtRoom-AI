from enum import Enum

class LLMProvider(str, Enum):
    GEMINI = "gemini"
    OPENAI = "openai"