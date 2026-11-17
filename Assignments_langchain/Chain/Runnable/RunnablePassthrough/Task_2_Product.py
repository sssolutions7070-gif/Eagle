import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 2: Product 
• Input: Product name.  
• Use RunnablePassthrough() to keep the original product name.  
• At the same time, generate a short description.  

"""
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough
from langchain_core.prompts import PromptTemplate

model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

prompt=PromptTemplate(
    template="give a short discripation about the product name{name}",
    input_variables=["name"]
)

parser=StrOutputParser()

dis_chain=prompt | model | parser


chain=RunnableParallel(
    original_name=RunnablePassthrough(),
    discription=dis_chain
)

res=chain.invoke("Suggar")

print("proudct name:",res["original_name"])
print("discription:",res["discription"])

