from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-pro-exp-02-05')

result = model.invoke('What is the capital of India?')

print(result.content)
