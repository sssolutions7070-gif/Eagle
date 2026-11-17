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


class OutPutStruct(BaseModel):
    name:Annotated[str,Field(description="This is the user name")]
    age:Annotated[int,Field(description="This is The User Age")]
    Contact:Annotated[int,Field(description="this is the user contact")]


output=model.with_structured_output(OutPutStruct)

res=output.invoke("My Name Is Satej I Am 23 Years Old My Contact Number Is 9156994716")

print(res)






