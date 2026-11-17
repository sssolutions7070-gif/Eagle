import os
from dotenv import load_dotenv
load_dotenv()

"""
4. Job Candidate Parser Create a prompt that generates candidate information in a fixed format. 
Input: Sneha is a Python developer with 3 years of experience. She knows Python, Django and SQL and expects 7 LPA. 
Expected LLM output: Name: Sneha Role: Python Developer Experience: 3 years Skills: Python, Django, SQL Expected Salary: 7 LPA 
Task: Use an output parser to extract the candidate information into separate variables.

"""

from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from pydantic import BaseModel,Field
from typing import Annotated
from langchain_core.output_parsers import PydanticOutputParser

model=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)
class JobCandidate(BaseModel):
    name:Annotated[str,Field(discription="this is the book name")]
    Author:Annotated[str,Field(discription="this is the Author name")]
    Pages:Annotated[int,Field(discription="THis is the pages count of the book")]
    category:Annotated[str,Field(discription="This is the Category of the Book")]


parser=PydanticOutputParser(pydantic_object=Library)

llm_model=ChatHuggingFace(llm=model)

prompt=f"Harry Potter was written by J.K. Rowling. It has 500 pages and belongs to the Fantasy category. {parser.get_format_instructions()}"

res=llm_model.invoke(prompt)

print(res.content)
