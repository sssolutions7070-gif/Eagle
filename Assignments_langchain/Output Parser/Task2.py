import os
from dotenv import load_dotenv
load_dotenv()

"""
2. Patient Information Parser Ask the LLM to generate patient information in a fixed text format. 
Input: Patient Ravi is 45 years old and has fever and cough. 
Expected LLM output: Name: Ravi Age: 45 Symptoms: Fever, Cough Task: Create an output parser that extracts Name, Age and Symptoms.

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

class patient_info(BaseModel):
    Name:Annotated[str,Field(description="this is patient name")]
    age:Annotated[int,Field(description="this is patient age")]
    Symptoms:Annotated[list[str],Field(description="this is patient Symptoms")]

parser=PydanticOutputParser(pydantic_object=patient_info)

llm_model=ChatHuggingFace(llm=model)

prompt=f"Patient Ravi is 45 years old and has fever and cough.{parser.get_format_instructions()}"

res=llm_model.invoke(prompt)


result = parser.parse(res.content)
print(result)