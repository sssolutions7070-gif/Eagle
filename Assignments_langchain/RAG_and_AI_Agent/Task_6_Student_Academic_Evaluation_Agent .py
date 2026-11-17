import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 6: Student Academic Evaluation Agent 
Create an AI agent that checks student exam eligibility and evaluates academic 
performance. 
Tools: 
1. AttendanceChecker(attendance) — checks whether attendance meets the 75% 
requirement. 
2. CalculatePercentage(obtained, total) — calculates marks percentage. 
3. CheckPassFail(percentage) — determines pass or fail using a 40% threshold. 
Sample Query: "My attendance is 82%, and I scored 380 out of 500. Check my exam 
eligibility and result."

"""

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

@tool
def attendance_checker(att:int)->str:
    """This Is the attendnce Checker"""
    if att>75:
        return "this student is elliible for the exam"
    else:
        return "this is not elligible for the exam"
    
@tool
def calculate_percentage(obtained_mark:int,total:int)->float:
    """THIS IS THE pecentage Checker"""
    return (obtained_mark*total)/100

@tool
def check_pass_fail(percentage:float) -> str:
    """this is chceking of the pass or the fail"""
    if percentage>40:
        return "this student is pass"
    else:
        return "this student is fail"


tools=[attendance_checker,calculate_percentage,check_pass_fail]

llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

llm_with_model=llm.bind_tools(tools)

question="""My attendance is 82%, and I scored 380 out of 500. Check my exam eligibility and result."""

res=llm_with_model.invoke(question)

for i in res.tool_calls:
    if i["name"]=="attendance_checker":
        response=attendance_checker.invoke(i["args"])
    elif i["name"]=="calculate_percentage":
        response=calculate_percentage.invoke(i["args"])
    elif i["name"]=="check_pass_fail":
        response=check_pass_fail.invoke(i["args"])

    print(i["name"],response)