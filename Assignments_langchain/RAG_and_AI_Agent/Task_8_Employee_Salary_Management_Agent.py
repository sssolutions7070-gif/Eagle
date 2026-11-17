import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 8: Employee Salary Management Agent 
Create an AI agent that calculates employee salary and checks bonus eligibility. 
Tools: 
1. CalculateGrossSalary(basic, allowances) — calculates gross salary. 
2. CalculateNetSalary(gross, deductions) — calculates net salary. 
3. CheckBonus(performance_score) — checks bonus eligibility using a defined score 
threshold of 80 out of 100. 
Sample Query: "My basic salary is ₹30,000, allowances are ₹5,000, deductions are ₹2,000, 
and my performance score is 85. Calculate my salary and check bonus eligibility." 

"""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool

@tool
def calculate_gross_salary(basic:int,allowance:int) -> str:
    """THis is the Gross Salary Finding there"""
    return f"The Gross Salary is{basic+allowance}"

@tool
def calculate_net_salary(gross: int, deductions: int) -> str:
    """Calculate the net salary as gross salary minus total deductions."""
    return f"The Net Salary is {gross - deductions}"
 

@tool
def check_bonus(performance_score: float) -> str:
    """Check whether an employee qualifies for a bonus. The threshold is 80 out of 100."""
    if performance_score >= 80:
        return "Employee qualifies for a bonus."
    else:
        return "Employee does not qualify for a bonus."


tools=[calculate_gross_salary,calculate_net_salary,check_bonus]

llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

llm_with_model=llm.bind_tools(tools)
question = """
An employee has a basic salary of ₹30,000 and allowances of ₹5,000.
The total deductions are ₹3,000, and the performance score is 85 out of 100.

1. Calculate the gross salary.
2. Calculate the net salary after deductions.
3. Check whether the employee qualifies for a bonus.
"""
res=llm_with_model.invoke(question)

print(res.tool_calls)


for i in res.tool_calls:
    if i["name"]=="calculate_gross_salary":
        result=calculate_gross_salary.invoke(i["args"])
    elif i["name"]=="calculate_net_salary":
        result=calculate_net_salary.invoke(i["args"])
    elif i["name"]== "check_bonus":
        result=check_bonus.invoke(i["args"])
    
    print(i["name"],":",result)