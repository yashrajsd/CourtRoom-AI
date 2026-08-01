import asyncio
from langchain_core.messages import HumanMessage
from app.llm.factory import LLMFactory
from app.llm.service import LLMService
from app.schemas.evaluation import EvaluationResultSchema


async def main():
    llm = LLMFactory.create()
    service = LLMService(llm)

    response = await service.structured_chat(
            messages=[
                HumanMessage(
                    content="""
                            Decide whether to continue questioning or proceed.

                            Return the decision.
                            """
                )
            ],
            schema=EvaluationResultSchema,
        )

    print(response)
    print(type(response))


if __name__ == "__main__":
    asyncio.run(main())
