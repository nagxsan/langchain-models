from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    'Superman is the latest DCEU movie.',
    'New Delhi is the capital of India',
    'AI is the latest boom in software industry.'
]

result = embedding.embed_documents(documents)

print(str(result))