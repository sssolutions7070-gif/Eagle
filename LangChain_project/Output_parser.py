import os
from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from pydantic import BaseModel,Field
from typing import Annotated
from langchain_core.output_parsers import PydanticOutputParser 

model=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

class PersontStruct(BaseModel):
    name:Annotated[str,Field(description="this is user name")]
    age:Annotated[int,Field(description="this is user age")]
    contact:Annotated[int,Field(description="this is user contact")]

parser= PydanticOutputParser(pydantic_object=PersontStruct)

llm_model=ChatHuggingFace(llm=model)

prompt=f"my name is demouser my age is 22 contact number is 89898989{parser.get_format_instructions()}"

result=llm_model.invoke(prompt)

print(result.content)