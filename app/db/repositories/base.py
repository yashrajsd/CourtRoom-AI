from typing import Generic,TypeVar
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    """
    Base repository implementing common CRUD operation
    """

    def __init__(
            self,
            session: AsyncSession,
            model: type[ModelType],
    ):
        self.session =  session
        self.model = model

    async def get(self,id):
        stmt = select(self.model).where(
            self.model.id ==id
        )

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def create(
            self,
            entity: ModelType
    )-> ModelType:
        
        self.session.add(entity)
        return entity

    async def delete(
            self,
            entity: ModelType
    ):
        await self.session.delete(entity)
        await self.session.commit()

    async def list(self):
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return list(result.scalar().all())