import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 1: Greeting 
• Input: Name 
• Step 1: Generate a greeting.  
• Step 2: Generate a short message using the greeting. 
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

prompt=PromptTemplate.from_template(
    "Generate a friendly greeting for a person named {name}."
)

prompt1=PromptTemplate.from_template(
    "Using the greeting '{greeting}', generate a short, friendly message."
)

chain=RunnableSequence(prompt,model,parser)
chain1=RunnableSequence(prompt1,model,parser)

name=input("Please Enter Input as Name Field")
res1=chain.invoke({
    "name":name
})
print(res1)

res2=chain1.invoke({
    "greeting":res1
})
print(res2)