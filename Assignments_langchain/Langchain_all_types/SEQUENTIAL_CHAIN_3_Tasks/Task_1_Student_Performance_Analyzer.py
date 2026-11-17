import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 1: Student Performance Analyzer Objective: 
Create a Sequential Chain that analyzes a student's academic performance. 
Requirements: 
• Take a student's name, marks, and total marks as input. 
• Create the first chain to calculate the percentage and identify the performance level. 
• Create the second chain to generate personalized improvement suggestions based on the first chain's output. 
• Connect both chains sequentially so that the output of the first chain becomes the input of the second chain. 
• Display the percentage, performance level, and improvement suggestions. 

"""


from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

parser=StrOutputParser()

prompt1=PromptTemplate.from_template(
    """
    this is the student acedamic performance checker

    studnet name:{name}
    student marks:{marks}
    total marks:{total_marks}

    now this is using the toatl marks we can find the percentage of the 
    percentage=(obtained matks/total matks)*100

    now we are identify the performace level using:
    90-100%=Excellent
    80-89%=Very Good
    70-79%=good
    40-69%=Average
    below 40%=Needs the improvement
    
    return =
    student Name:
    percentage:
    performace level:

    """
)

performance_anlysis= prompt1 | model | parser

prompt2=PromptTemplate.from_template(
    """
    as per the student performace

    {performance_anlysis}

    Generate a personalized imporvemnt suggestion for the student 
    Include:
    1. Study improvement tips.
    2. Time management suggestions.
    3. Subjects to focus on.
    4. Daily study routine.
    5. Motivational advice.

    Give simple and practical suggestions.

    """
)

imporvment_suggestion=prompt2| model| parser

prompt3=PromptTemplate.from_template(
    """
    

    """
)