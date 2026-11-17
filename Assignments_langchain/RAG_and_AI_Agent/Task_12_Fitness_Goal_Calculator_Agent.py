import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 12: Fitness Goal Calculator Agent 
Create an AI agent that calculates basic fitness metrics and checks exercise goals. 
Tools: 
1. CalculateBMI(weight_kg, height_m) — calculates BMI. 
2. CalculateWeeklyExercise(total_minutes, days) — calculates average exercise 
minutes per day. 
3. CheckExerciseGoal(total_minutes, target_minutes) — checks whether the user's 
exercise time meets a defined target. 
Sample Query: "My weight is 70 kg, my height is 1.75 metres, and I exercised for 150 
minutes over 5 days. Calculate my BMI and check whether I met my 150-minute weekly 
exercise target." 


"""

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

@tool
def calculate_bmi(weight_kg: float, height_m: float) -> str:
    """Calculate BMI using weight in kg and height in metres."""
    bmi = weight_kg / (height_m ** 2)
    return f"BMI = {bmi:.2f}"


@tool
def calculate_weekly_exercise(total_minutes: int, days: int) -> str:
    """Calculate average exercise minutes per day."""
    if days <= 0:
        return "Error: Days must be greater than zero."

    average = total_minutes / days
    return f"Average exercise per day = {average:.2f} minutes"


@tool
def check_exercise_goal(total_minutes: int, target_minutes: int) -> str:
    """Check whether total exercise minutes meet the weekly target."""
    if total_minutes >= target_minutes:
        return (
            f"Goal achieved: {total_minutes} minutes meets "
            f"the {target_minutes}-minute weekly target."
        )
    else:
        remaining = target_minutes - total_minutes
        return f"Goal not achieved. Exercise {remaining} more minutes."


tools=[calculate_bmi,calculate_weekly_exercise,check_exercise_goal]
llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

llm_with_model=llm.bind_tools(tools)
# Sample query
question = """
My weight is 70 kg, my height is 1.75 metres,
and I exercised for 150 minutes over 5 days.

1. Calculate my BMI.
2. Calculate my average exercise minutes per day.
3. Check whether I met my 150-minute weekly exercise target.
"""

res = llm_with_model.invoke(question)
print(res.tool_calls)


for i in res.tool_calls:
    if i["name"]=="calculate_bmi":
        result=calculate_bmi.invoke(i["args"])
    elif i["name"]=="calculate_weekly_exercise":
        result=calculate_weekly_exercise.invoke(i["args"])
    elif i["name"]=="check_exercise_goal":
        result=check_exercise_goal.invoke(i["args"])

    print(i["name"],":",result)









    