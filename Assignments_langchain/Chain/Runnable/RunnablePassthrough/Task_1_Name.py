import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 1: Name 
• Input: Student name.  
• Use RunnablePassthrough() to keep the original name.  
• At the same time, generate a short introduction.  
"""



from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableParallel
from langchain_core.output_parsers import StrOutputParser 

model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

prompt=PromptTemplate(
    template="Give a short introduction for a student named {name}.",
    input_variables=["name"]
)

parser=StrOutputParser()

intro_chain=prompt | model | parser

chain=RunnableParallel(
    ORigianl_name=RunnablePassthrough(),
    intoduction=intro_chain
    
)

res=chain.invoke("Satej Rajeshirke")
print("original name:",res["ORigianl_name"])
print("introduction:",res["intoduction"])
