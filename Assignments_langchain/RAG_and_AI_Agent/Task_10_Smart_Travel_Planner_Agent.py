import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 10: Smart Travel Planner Agent 
Create an AI agent that calculates trip costs and checks whether the trip fits the available 
budget. 
Tools: 
1. CalculateTravelCost(transport, hotel, food) — calculates the total trip cost. 
2. CalculateCostPerPerson(total_cost, people) — calculates the cost per person. 
3. CheckBudget(total_cost, budget) — checks whether the trip is within budget. 
Sample Query: "Transport costs ₹5,000, hotel costs ₹8,000, and food costs ₹3,000. Four 
people are travelling, and our budget is ₹20,000. Calculate the total cost, cost per person, 
and budget status." 

"""

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

@tool 
def calculate_travel_cost(transport:int,hotel:int,food:int) -> str:
    """this is gives the total cost for that """
    return f"This find the total traval cost{transport+hotel+food}"

@tool
def calculate_cost_per_person(total_cost:int,people:int) ->str:
    """This is gives the cost per person"""
    return f"This find the total cost {total_cost/people}"

@tool
def check_budget(total_cost:int,budget:int) ->str:
    """this is check the Budget"""
    if budget>=total_cost:
        return "this is in the Budget"
    else:
        return "this is is not in budget"


tools=[calculate_travel_cost,calculate_cost_per_person,check_budget]
llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

llm_with_model=llm.bind_tools(tools)
question = """
I am planning a trip with 4 people.
The transport cost is ₹8,000, the hotel cost is ₹12,000,
and the food cost is ₹4,000.
Our total trip budget is ₹30,000.

1. Calculate the total estimated travel cost.
2. Calculate the cost per person.
3. Check whether the trip is within our budget.
4. Give me a short summary of the travel expenses.
"""
res = llm_with_model.invoke(question)
print(res.tool_calls)


for i in res.tool_calls:
    if i["name"]=="calculate_travel_cost":
        result=calculate_travel_cost.invoke(i["args"])
    elif i["name"]=="calculate_cost_per_person":
        result=calculate_cost_per_person.invoke(i["args"])
    elif i["name"]=="check_budget":
        result=check_budget.invoke(i["args"])

    print(i["name"],":",result)









    