import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from pydantic import BaseModel,Field
from typing import Annotated


model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

class OutputStruct(BaseModel):
    name:Annotated[str,Field(description="this is the user name")]
    age:Annotated[int,Field(description="this is the user age")]
    contact:Annotated[int,Field(description="this is the user Contact")]

output_format=model.with_structured_output(OutputStruct)

res= output_format.invoke("my name is satej and my age is 23 and my contact number is 9156994716")

print(res)