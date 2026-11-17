import os
from dotenv import load_dotenv
load_dotenv()

"""
1. Student Result Parser Create a prompt that asks the LLM to generate a student's result.
Input: Student Rahul has scored 85 in Python, 78 in JavaScript and 90 in DBMS. 
Expected LLM output: Name: Rahul Python: 85 JavaScript: 78 DBMS: 90 Total: 253 Percentage: 84.33 
Task: Use an output parser to parse the LLM response and extract each value separately.

"""

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from pydantic import BaseModel,Field
from typing import Annotated
from langchain_core.output_parsers import PydanticOutputParser

model=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

class StudentResult(BaseModel):
    Name:Annotated[str,Field(description="this is student name")]
    Python:Annotated[int,Field(description="this is student python marks")]
    JavaScript:Annotated[int,Field(description="this is javascript marks")]
    DBMS:Annotated[int,Field(description="this is DBMS Marks")]
    Total:Annotated[int,Field(description="This is total")]
    Percentage:Annotated[float,Field(description="this is percenatge")]


parser=PydanticOutputParser(pydantic_object=StudentResult)
llm_model=ChatHuggingFace(llm=model)

prompt=f"tudent Rahul has scored 85 in Python, 78 in JavaScript and 90 in DBMS.{parser.get_format_instructions()}"

res=llm_model.invoke(prompt)
print(res.content)

