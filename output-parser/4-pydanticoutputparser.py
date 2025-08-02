from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

class Person(BaseModel):

    name: str = Field(description='Name of the person')
    age: int = Field(description='Age of the person', ge=18, le=120)
    city: str = Field(description='City of the person')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Give me the name, age and country of a fictional person from country {country}.\n{instructions}',
    input_variables=['country'],
    partial_variables={ 'instructions': parser.get_format_instructions() }
)

chain = template | model | parser

data = chain.invoke({ 'country': 'France' })

print(data)
