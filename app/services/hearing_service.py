from app.db.unir_of_work import UnitOfWork
from app.db.models.hearing import Hearing
from  app.db.models.message import Message
from app.core.enums import HearingStatus,MessageRole

class HearingService:

    async def create_hearing(
            self,
            title:str,
            description:str,
            category:str,
            user_id,
    )-> Hearing:

        async with UnitOfWork as uow:
            hearing = Hearing(
                title = title,
                description = description,
                category = category,
                user_id = user_id,
                staus = HearingStatus.CREATED
            )

            uow.hearings.add(hearing)

            message = Message(
                hearing = hearing,
                role = MessageRole.USER,
                content = description
            )

            uow.message.add(message)

            await uow.session.flush()
            await uow.session.refresh(hearing)

            return hearing