import os
from dotenv import load_dotenv
load_dotenv()

"""
1. Student Management System Create a LangChain prompt that takes a student's information and returns structured output.
Input example: My name is Rahul, I am 21 years old, studying Computer Science in 3rd year, and 
my percentage is 78.5. 
Expected structure: name → string; age → integer; course → string; year → integer; percentage → number.
 Task: Define a suitable Pydantic structure and make the LLM return the information according to the schema.
"""

from langchain_groq import ChatGroq
from pydantic import BaseModel,Field
from typing import Annotated


model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)


class Studentstruct(BaseModel):
    name:Annotated[str,Field(description="this is student name ")]
    age:Annotated[int,Field(description="This is student age")]
    course:Annotated[str,Field(description="This is student course")]
    year:Annotated[int,Field(description="this is student year")]
    percentage:Annotated[float,Field(description="this is student percentage")]


output_format=model.with_structured_output(Studentstruct)

res=output_format.invoke("My name is Rahul, I am 21 years old, studying Computer Science in 3rd year, and my percentage is 78.5.")

print(res)