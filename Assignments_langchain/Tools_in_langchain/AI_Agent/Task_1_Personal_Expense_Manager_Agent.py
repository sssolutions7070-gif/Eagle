import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 1: Personal Expense Manager Agent 
Beginner–Intermediate 
Objective: Create an agent that calculates expenses and identifies spending habits. 
Tools to create: 
1. CalculateTotal(food, travel, shopping) — calculates total expenses. 
2. AnalyzeSpending(food, travel, shopping) — identifies the category with the highest 
spending. 
3. CheckBudget(total_expense, budget) — checks whether the user is within budget.

"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool 

@tool
def calculatetotal(food:float,travel:float,shopping:float) -> float:
    """this is the calulate total expenses there"""
    return (food+travel+shopping)


@tool
def analyzespending(food:float,travel:float,shopping:float) -> str:
    """this is the alyzes the spending and then it is calulated highest expence"""
    if food>=travel and food>=shopping:
        return f"food has the high expense{food}"
    elif shopping>=travel and shopping>=food:
        return f"Shoppings has the high expense{shopping}"
    else:
        return f"Travel has the high expense{travel}"

@tool
def checkbudget(total_expense: float, budget: float) -> str:
    """Check whether expenses are within budget."""
    if total_expense <= budget:
        return f"This is within the budget. Budget: ₹{budget}"
    else:
        return f"This is over budget. Budget: ₹{budget}"

    
llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

tools=[calculatetotal,checkbudget,analyzespending]
llm_with_model=llm.bind_tools(tools)

question = """
I spent ₹2000 on food, ₹1500 on travel, and ₹3000 on shopping.
My monthly budget is ₹7000.

1. Calculate my total expenses.
2. Identify which category has the highest spending.
3. Check whether I am within my budget.
4. Give me a short analysis of my spending habits.
"""

res=llm_with_model.invoke(question)
print(res.tool_calls)

for i in res.tool_calls:
    if i["name"]=="calculatetotal":
        result=calculatetotal.invoke(i["args"])
    elif i["name"]=="analyzespending":
        result=analyzespending.invoke(i["args"])
    elif i["name"]=="checkbudget":
        result=checkbudget.invoke(i["args"])

    print(i["name"],":",result)