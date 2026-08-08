from uuid import UUID

from sqlalchemy import Enum, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimeStampMixin, UUIDPrimaryMixin
from app.core.enums import MessageRole
from app.db.models.hearing import Hearing
from sqlalchemy.orm import relationship


class Message(Base, UUIDPrimaryMixin, TimeStampMixin):
    __tablename__ = "messages"

    hearing_id: Mapped[UUID] = mapped_column(
        ForeignKey("hearings.id", ondelete="CASCADE"),
        nullable=False,
    )

    role: Mapped[MessageRole] = mapped_column(
        Enum(MessageRole),
        nullable=False,
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    hearing: Mapped[Hearing] = relationship(
        back_populates="messages"
    )