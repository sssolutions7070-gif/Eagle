import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 9: E-commerce Order Management Agent 
Create an AI agent that calculates product costs, applies discounts, and checks free 
delivery eligibility. 
Tools: 
1. CalculateOrderTotal(price, quantity) — calculates the original order total. 
2. ApplyDiscount(total, discount_percentage) — calculates the discounted amount. 
3. CheckFreeDelivery(order_amount) — checks free delivery eligibility for orders of at 
least ₹1,000. 
Sample Query: "I want 3 products costing ₹500 each. Apply a 10% discount and check free 
delivery eligibility." 

"""

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI 


@tool
def calculate_order_total(price: float, quantity: float) -> float:
    """Calculate the total product cost."""
    return price * quantity
@tool
def apply_discount(total:float,discount_percentage:float)->str:
    """this is the discount method to check the discount there"""
    discount_amount = total * discount_percentage / 100
    final_amount = total - discount_amount
    return f"Discounted price is ₹{final_amount}"

@tool
def check_free_delivery(order_amount: float) -> str:
    """Check whether the order qualifies for free delivery."""
    if order_amount >= 1000:
        return "Customer is eligible for free delivery."
    else:
        return "Customer is not eligible for free delivery."

llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

question = """
I purchased 2 products, each costing ₹800.
Apply a discount of 10%.

1. Calculate the total order amount.
2. Apply the 10% discount and calculate the final amount.
3. Check whether the order is eligible for free delivery.
4. Give me a short summary of the order bill.
"""

tool=[calculate_order_total,apply_discount,check_free_delivery]
llm_with_model=llm.bind_tools(tool)


res=llm_with_model.invoke(question)
print(res.tool_calls)
for i in res.tool_calls:
    if i["name"]=="calculate_order_total":
        result=calculate_order_total.invoke(i["args"])
    elif i["name"]=="apply_discount":
        result=apply_discount.invoke(i["args"])
    elif i["name"]=="check_free_delivery":
        result=check_free_delivery.invoke(i["args"])

    print(i["name"],":",result)




    

