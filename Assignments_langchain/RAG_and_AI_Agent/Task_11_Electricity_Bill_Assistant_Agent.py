import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 11: Electricity Bill Assistant Agent 
Create an AI agent that calculates an electricity bill and identifies high consumption. 
Tools: 
1. CalculateElectricityBill(units, rate) — calculates the energy charge. 
2. AddFixedCharge(amount, fixed_charge) — adds a fixed charge. 
3. CheckHighConsumption(units, threshold) — checks whether electricity 
consumption exceeds a defined threshold. 
Sample Query: "I used 250 electricity units at ₹8 per unit, with a fixed charge of ₹100. 
Calculate my bill and check whether consumption exceeds 200 units."

"""


from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

@tool
def calculate_electricity_bill(units: int, rate: int) -> str:
    """Calculate the electricity energy charge using units and rate per unit."""
    bill = units * rate
    return f"Energy charge = ₹{bill}"


@tool
def add_fixed_charge(amount: int, fixed_charge: int) -> str:
    """Add the fixed charge to the electricity energy charge."""
    total_bill = amount + fixed_charge
    return f"Total electricity bill = ₹{total_bill}"


@tool
def check_high_consumption(units: int, threshold: int) -> str:
    """Check whether electricity consumption exceeds the given threshold."""
    if units > threshold:
        return f"High consumption: {units} units exceeds {threshold} units."
    else:
        return f"Normal consumption: {units} units does not exceed {threshold} units."


tools=[calculate_electricity_bill,add_fixed_charge,check_high_consumption]
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
    if i["name"]=="calculate_electricity_bill":
        result=calculate_electricity_bill.invoke(i["args"])
    elif i["name"]=="add_fixed_charge":
        result=add_fixed_charge.invoke(i["args"])
    elif i["name"]=="check_high_consumption":
        result=check_high_consumption.invoke(i["args"])

    print(i["name"],":",result)









    