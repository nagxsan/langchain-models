from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Annotated, TypedDict

load_dotenv()

model = ChatOpenAI(model='gpt-4.1-nano')

# schema
class Review(TypedDict):
    summary: Annotated[str, "a brief summary of the review"]
    sentiment: Annotated[str, "the sentiment of the review: positive, negative or mixed"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("The hardware is great but the software feels bloated. Also given the amount of RAM that the device has, it feels unnaturally slow to move through. Although when gaming mode is switched on, it operates pretty well for a device in this price range.")

print(result)