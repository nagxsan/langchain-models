from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4.1-nano', temperature=0)

result = model.invoke('Suggest 5 Indian male names.')

print(result.content)