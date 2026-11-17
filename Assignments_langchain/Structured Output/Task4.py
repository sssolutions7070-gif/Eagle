import os
from dotenv import load_dotenv
load_dotenv()

"""
4. Job Applicant Management Create a structured-output system that extracts job applicant information. 
Input example: My name is Amit Patil. I have 2 years of experience in React and Node.js. I am expecting a salary of 6 LPA and can join immediately. 
Expected structure: name → string; experience → integer; skills → list of strings; expected_salary → number; immediate_joiner → boolean. 
Task: Define a suitable Pydantic structure and make the LLM return the information according to the schema.

"""

from langchain_groq import ChatGroq
from pydantic import BaseModel,Field
from typing import Annotated

model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)


class JobStruct(BaseModel):
    name:Annotated[str,Field(description="this is job applicant name")]
    experience:Annotated[int,Field(description="this is job applicant Experience")]
    skills:Annotated[list[str],Field(description="this is job applicatnt skills")]
    expected_salary:Annotated[int,Field(description="this is job applicant expected salary")]
    immediate_joiner:Annotated[bool,Field(description="this is job applicant joiner status")]

output_textures=model.with_structured_output(JobStruct)

res=output_textures.invoke(" My name is Amit Patil. I have 2 years of experience in React and Node.js. I am expecting a salary of 6 LPA and can join immediately.")

print(res)