import asyncio

from langchain_core.messages import HumanMessage

from app.llm.factory import LLMFactory
from app.llm.service import LLMService
from app.schemas.evaluation import EvaluationResultSchema


async def main():
    llm = LLMFactory.create()
    llm_service = LLMService(llm)

    messages = [
        HumanMessage(
            content="""
The user says:

"I was terminated from my job without any prior notice.
My employer also refused to pay my final month's salary."

Should the lawyer continue asking questions,
or is there enough information to proceed
to the opposing counsel?

Respond using the EvaluationResult schema.
"""
        )
    ]

    result = await llm_service.structured_chat(
        messages=messages,
        schema=EvaluationResultSchema,
    )

    print("Evaluation Result")
    print("-----------------")
    print(result)

    print("\nNext Step:", result.next_step)
    print("Reason:", result.reason)


if __name__ == "__main__":
    asyncio.run(main())