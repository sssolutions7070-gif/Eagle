import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI



@tool
def add(a:int ,b:int) -> int:
    """this is the addition method"""
    return a + b

llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


llm_with_tools=llm.bind_tools([add])


res=llm_with_tools.invoke("what is the addition of 30 + 20?")

print(res.tool_calls)

for call in res.tool_calls:
    result=add.invoke(call["args"])
    print(result)