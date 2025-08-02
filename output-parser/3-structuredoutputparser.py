from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4.1-nano')

output_schema = [
    ResponseSchema(name='name', description='Name of the fictional person'),
    ResponseSchema(name='age', description='Age of the person'),
    ResponseSchema(name='country', description='Country of the person')
]

parser = StructuredOutputParser.from_response_schemas(output_schema)

template = PromptTemplate(
    template='Give me the name, age and country of a fictional person.\n{instructions}',
    input_variables=[],
    partial_variables={ 'instructions': parser.get_format_instructions() }
)

chain = template | model | parser

data = chain.invoke({})

print(data)
