from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import SessionLocal
from app.db.repositories.hearing import HearingRepository
from app.db.repositories.message import MessageRepository

class UnitOfWork:

    def __init__(self):
        self.session: AsyncSession | None = None
        self.hearings: HearingRepository | None = None
        self.messages: MessageRepository | None = None

    async def __aenter__(self):
        self.session = SessionLocal()
        self.hearings = HearingRepository(self.session)
        self.messages = MessageRepository(self.session)

        return self

    async def __aexit__(
            self,
            exc_type,
            exc,
            tb
    ):
        if exc is None:
            await self.session.commit()
        else:
            await self.session.rollback()
        await self.session.close()