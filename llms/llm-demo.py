from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-4.1-nano')

result = llm.invoke("What is the latest MCU movie? Just give me a single line answer.")

print(result)