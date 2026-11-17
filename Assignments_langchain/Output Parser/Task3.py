import os
from dotenv import load_dotenv
load_dotenv()

"""
3. Library Book Parser Create a prompt that generates book information in a predefined format.
Input: Harry Potter was written by J.K. Rowling. It has 500 pages and belongs to the Fantasy category. 
Expected LLM output: Book: Harry Potter Author: J.K. Rowling Pages: 500 Category: Fantasy 
Task: Use an output parser to extract the four fields from the LLM response.

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
class Library(BaseModel):
    Book:Annotated[str,Field(discription="this is the book name")]
    Author:Annotated[str,Field(discription="this is the Author name")]
    Pages:Annotated[int,Field(discription="THis is the pages count of the book")]
    category:Annotated[str,Field(discription="This is the Category of the Book")]


parser=PydanticOutputParser(pydantic_object=Library)

llm_model=ChatHuggingFace(llm=model)

prompt=f"Harry Potter was written by J.K. Rowling. It has 500 pages and belongs to the Fantasy category. {parser.get_format_instructions()}"

res=llm_model.invoke(prompt)

print(res.content)