import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI


llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

@tool
def add(a:int,b:int):
    """This is the addition of the Two numbers"""
    return a+b

llm_with_model=llm.bind_tools([add])

response=llm_with_model.invoke("What is 10 + 20?")

print(response.tool_calls)

for call in response.tool_calls:
    result=add.invoke(call["args"])
    print(result)

