from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4.1-nano')

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me the name, age and city of a fictional person.\n{instructions}',
    input_variables=[],
    partial_variables={ 'instructions': parser.get_format_instructions() }
)

chain = template | model | parser

data = chain.invoke({})

print(data)
