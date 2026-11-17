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
def add(a:int,b:int) -> int:
    """this is the addition operation"""
    return a+b

llm_with_model=llm.bind_tools([add])

result=llm_with_model.invoke("Please add tell me addition of 10+20")

print(result.tool_calls)

for i in result.tool_calls:
    res=add.invoke(i["args"])
    print(res)