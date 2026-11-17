import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 14: Banking Savings Planner Agent 
Create an AI agent that calculates monthly savings and estimates future savings. 
Tools: 
1. CalculateMonthlySavings(income, expenses) — calculates monthly savings. 
2. CalculateSavingsRate(savings, income) — calculates savings as a percentage of 
income. 
3. ProjectSavings(monthly_savings, months) — estimates savings over a specified 
period. 
Sample Query: "My monthly income is ₹40,000 and my expenses are ₹28,000. Calculate 
my savings rate and estimate my savings over 12 months, assuming the same monthly 
savings." 


"""
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

@tool
def calculate_monthly_savings(income: float, expenses: float) -> str:
    """Calculate monthly savings using income and expenses."""
    savings = income - expenses
    return f"Monthly savings = ₹{savings:.2f}"


# Tool 2: Calculate savings rate
@tool
def calculate_savings_rate(savings: float, income: float) -> str:
    """Calculate savings as a percentage of income."""
    if income <= 0:
        return "Error: Income must be greater than zero."

    rate = (savings / income) * 100
    return f"Savings rate = {rate:.2f}%"

@tool
def project_savings(monthly_savings: float, months: int) -> str:
    """Estimate total savings over a given number of months."""
    if months < 0:
        return "Error: Months cannot be negative."

    total_savings = monthly_savings * months
    return f"Projected savings for {months} months = ₹{total_savings:.2f}"


tools=[calculate_monthly_savings,calculate_savings_rate,project_savings]
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
    if i["name"]=="calculate_monthly_savings":
        result=calculate_monthly_savings.invoke(i["args"])
    elif i["name"]=="calculate_savings_rate":
        result=calculate_savings_rate.invoke(i["args"])
    elif i["name"]=="project_savings":
        result=project_savings.invoke(i["args"])

    print(i["name"],":",result)


    









    
