from pathlib import Path

class PromptLoader:
    "Loads prompt templates from the prompts directory"

    _PROMPTS_DIR = Path(__file__).parent

    @classmethod
    def load(cls,name:str)->str:
        prompt_path = cls._PROMPTS_DIR / f"{name}.md"

        if not prompt_path.exists():
            raise FileNotFoundError(f"Prompt template '{name}' not found in {cls._PROMPTS_DIR}")

        return prompt_path.read_text(encoding="utf-8")