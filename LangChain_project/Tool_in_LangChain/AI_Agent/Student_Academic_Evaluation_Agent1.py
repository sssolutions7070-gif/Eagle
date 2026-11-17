import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

@tool
def attendence_check(att:int) -> int:
    """this is the attendence checker"""
    if att>75:
        return "This is Elligible For the Exam"
    else:
        return "This is NOt Elligible For The exam"

@tool
def evaluation_check(ob_marks:int,total:int) -> float:
    """this is the evaluation check"""
    return (ob_marks/total)*100


tools=[attendence_check,evaluation_check]


llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

llm_with_model=llm.bind_tools(tools)

question="""i have 80% attendance can i eligible for exam """ 

res=llm_with_model.invoke(question)


for i in res.tool_calls:
    if i["name"]=="attendence_check":
        result=attendence_check.invoke(i["args"])
    elif i["name"]=="evaluation_check":
        result=evaluation_check.invoke(i["args"])
    
print(i["name"],":",result)
