from enum import Enum

class NextStep(str, Enum):
    LAWYER = "lawyer"
    OPPONENT = "opponent"
    JUDGE = "judge"
    END = "end"
