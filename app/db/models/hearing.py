from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped,mapped_column
from app.db.base import Base
from sqlalchemy import Enum
from app.core.enums import HearingStatus
from app.db.mixins import UUIDPrimaryMixin, TimeStampMixin
from sqlalchemy.orm import relationship

class Hearing(Base, UUIDPrimaryMixin, TimeStampMixin):
    __tablename__ = "Hearing"

    title: Mapped[str] = mapped_column(
        String(256),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    status: Mapped[HearingStatus] = mapped_column(
        Enum(HearingStatus),
        default=HearingStatus.CREATED
    )

    messages: Mapped[list["Message"]] = relationship(
        back_populates="hearing",
        cascade="all, delete-orphan",
    )
