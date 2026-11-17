import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 7: Personal Expense Manager Agent 
Create an AI agent that calculates expenses and analyzes spending. 
Tools: 
1. CalculateTotal(food, travel, shopping) — calculates total expenses. 
2. AnalyzeSpending(food, travel, shopping) — identifies the highest spending category. 
3. CheckBudget(total_expense, budget) — checks whether spending exceeds the 
budget. 
Sample Query: "I spent ₹2,000 on food, ₹1,000 on travel, and ₹2,500 on shopping. My 
budget is ₹5,000. Analyze my spending." 

"""


from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

@tool
def calculate_total(food: int, travel: int, shopping: int) -> int:
    """This tool calculates the total expenses."""
    return food + travel + shopping
  
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


tools=[calculate_total,analyzespending,checkbudget]

llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

llm_with_model=llm.bind_tools(tools)

question="""My attendance is 82%, and I scored 380 out of 500. Check my exam eligibility and result."""

res=llm_with_model.invoke(question)

for i in res.tool_calls:
    if i["name"]=="calculate_total":
        response=calculate_total.invoke(i["args"])
    elif i["name"]=="analyzespending":
        response=analyzespending.invoke(i["args"])
    elif i["name"]=="checkbudget":
        response=checkbudget.invoke(i["args"])

    print(i["name"],response)