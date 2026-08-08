from sqlalchemy import select
from app.db.models.message import Message
from app.db.repositories.base import BaseRepository

class MessageRepository(BaseRepository[Message]):

    def __init__(
            self,
            session
    ):
        super().__init__(session,Message)

    async def get_by_hearing(
            self,
            hearing_id
    ):
        stmt = (
            select(Message).where(Message.hearing_id==hearing_id).order_by(Message.created_at)
        )
        result = await self.session.execute(stmt)
        return list(result.scalar())
