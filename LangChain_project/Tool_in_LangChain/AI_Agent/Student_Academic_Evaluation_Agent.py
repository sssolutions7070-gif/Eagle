import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import tool
from langchain_google_genai  import ChatGoogleGenerativeAI

@tool
def attendce_check(attendence:int) -> str:
    """THis is the Attendence Cheker System"""
    if attendence>75:
        return "You Are Elligible For The Exam"
    else:
        return "You Are Not Elligible"

@tool
def evalution_check(ob_marks:int ,total:int) -> float:
    """this is the perentage checker"""
    return (ob_marks/total) * 100

llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

tools=[attendce_check,evalution_check]

llm_with_tool=llm.bind_tools(tools)

question="""i have 90% attendance can i eligible for exam """ 

res=llm_with_tool.invoke(question)

for i in res.tool_calls:
    if i["name"]=="attendce_check":
        respone=attendce_check.invoke(i["args"])

    elif i["name"]=="evalution_check":
        respone=evalution_check.invoke(i["args"])
    else:
        pass

print(i["name"],respone)