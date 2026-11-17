import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 2: Food 
• Input: Food name  
• Step 1: Generate a short description.
• Step 2: Generate 3 benefits using the description.  
"""


from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence 


model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)


parser=StrOutputParser()

prompt1=PromptTemplate.from_template(
    " Generate a short description of {food_name}"
)

prompt2=PromptTemplate.from_template(
    "Generate 3 benefits using the description{description}"
)

chain=RunnableSequence(prompt1,model,parser)
chain2=RunnableSequence(prompt2,model,parser)

food_name=input("Please Enter the Food Name:")

res=chain.invoke({
    "food_name":food_name
})

res2=chain2.invoke({
    "description":res
})

print(res)
print(res2)