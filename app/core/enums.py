from enum import Enum

class NextStep(str, Enum):
    LAWYER = "lawyer"
    OPPONENT = "opponent"
    JUDGE = "judge"
    END = "end"

class HearingStatus(str,Enum):
    COMPLETED = "completed"
    CREATED = "created"
    ACTIVE = "active"
    WAITING_FOR_USER = "waiting_for_user"
    FAILED = "failed"

class MessageRole(str,Enum):
    USER = "user",
    LAWYER = "lawyer",
    OPPONENT = "opponent",
    JUDGE = "judge",
    SYSTEM = "system"