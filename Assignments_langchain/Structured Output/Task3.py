import os
from dotenv import load_dotenv
load_dotenv()

"""
3. Library Book Management Create a system that extracts book information from a user's message.
Input example: I want to issue the book Python Programming by Mark Lutz.It has 800 pages and belongs to the programming category. 
Expected structure: book_name → string; author → string; pages → integer; category → string; available → boolean. 
Task: Define a suitable Pydantic structure and make the LLM return the information according to the schema.
"""

from langchain_groq import ChatGroq
from pydantic import BaseModel,Field
from typing import Annotated

model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

class LibraryStruct(BaseModel):
    book_name:Annotated[str,Field(description="It refers to Book Name")]
    author:Annotated[str,Field(description="this is author name ")]
    pages:Annotated[int,Field(description="this is pages of book")]
    category:Annotated[str,Field(description="this is category")]
    available:Annotated[bool,Field(description="this  book is avilable")]


output_textures=model.with_structured_output(LibraryStruct)

res=output_textures.invoke("I want to issue the book Python Programming by Mark Lutz.It has 800 pages and belongs to the programming category.")

print(res)