import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 15: College Information Assistant Agent 
Create an AI agent that answers college-related questions and performs academic 
calculations. 
Tools: 
1. CheckAttendanceEligibility(attendance) — checks whether attendance meets a 
defined requirement. 
2. CalculateInternalMarks(obtained, maximum) — calculates internal assessment 
percentage. 
3. SearchCollegeFAQ(question) — searches a supplied collection of college FAQs. 
Sample Query: "My attendance is 80%, and I scored 36 out of 50 in internal assessment. 
Also, tell me which documents are required for college admission."

"""

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

@tool
def check_attendance_eligibility(attendance: float) -> str:
    """Check whether attendance meets the minimum requirement of 75%."""
    if attendance >= 75:
        return f"Eligible: Attendance is {attendance}%, meeting the 75% requirement."
    else:
        return f"Not eligible: Attendance is {attendance}%, below the 75% requirement."


@tool
def calculate_internal_marks(obtained: float, maximum: float) -> str:
    """Calculate internal assessment percentage."""
    if maximum <= 0:
        return "Error: Maximum marks must be greater than zero."

    if obtained < 0 or obtained > maximum:
        return "Error: Obtained marks must be between 0 and maximum marks."

    percentage = (obtained / maximum) * 100
    return f"Internal assessment percentage = {percentage:.2f}%"




tools=[check_attendance_eligibility,calculate_internal_marks]
llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

llm_with_model=llm.bind_tools(tools)

question = """
My monthly income is ₹40,000 and my expenses are ₹28,000.

1. Calculate my monthly savings.
2. Calculate my savings rate.
3. Estimate my savings over 12 months,
   assuming the same monthly savings.
"""

res = llm_with_model.invoke(question)
print(res.tool_calls)


for i in res.tool_calls:
    if i["name"]=="check_attendance_eligibility":
        result=check_attendance_eligibility.invoke(i["args"])
    elif i["name"]=="calculate_internal_marks":
        result=calculate_internal_marks.invoke(i["args"])
   
    print(i["name"],":",result)




    









    









