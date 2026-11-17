import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def add(a:int,b:int) ->int:
    """ THis is the addition Operations are performs there """
    return a+b

llm_with_model=llm.bind_tools([add])

responese=llm_with_model.invoke("what is the 10+20 Addition ?")

print(responese.tool_calls)

for i in responese.tool_calls:
    res=add.invoke(i["args"])
    print(res)
