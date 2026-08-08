from uuid import UUID
from sqlalchemy import select
from app.db.models.hearing import Hearing
from app.db.repositories.base import BaseRepository

class HearingRepository(BaseRepository[Hearing]):

    def __init__(self,session):
        super().__init__(session,Hearing)

    async def get_active(
            self,
            hearing_id: UUID
    )-> Hearing | None:
        stmt = (
            select(Hearing).where(Hearing.id == hearing_id)
        )

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()
        