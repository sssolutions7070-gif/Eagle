import os
from dotenv import load_dotenv
load_dotenv()

"""
2. Patient Management System Create a structured-output system that extracts patient information from a natural-language prompt.
Input example: Patient name is Priya Sharma, age 35, suffering from fever and headache. Her blood group is O+.
Expected structure: patient_name → string; age → integer; symptoms → list of strings; blood_group → string.
Task: Define a suitable Pydantic structure and make the LLM return the information according to the schema.
"""

from langchain_groq import ChatGroq
from pydantic import BaseModel,Field
from typing import Annotated


model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

class Outputstruct(BaseModel):
    name:Annotated[str,Field(description="Patient Name")]
    age:Annotated[int,Field(description="patient Age")]
    symptoms:Annotated[list[str],Field(description="patient symptoms")]
    blood_group:Annotated[str,Field(description="patient blood_group")]

output_texture=model.with_structured_output(Outputstruct)

res=output_texture.invoke("Patient name is Priya Sharma, age 35, suffering from fever and headache. Her blood group is O+.")
print(res)