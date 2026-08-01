from app.llm.factory import LLMFactory

llm = LLMFactory.create()

response = llm.invoke("Say Hi in one sentense")

print(response.content)