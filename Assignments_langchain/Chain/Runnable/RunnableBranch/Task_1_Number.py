import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 1: Number 
• Input: A number.  
• If number is greater than 50 → print "Number is greater than 50".  
• Otherwise → print "Number is 50 or less".  

"""

from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableBranch,RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

parser=StrOutputParser()

model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)


prompt=ChatPromptTemplate.from_template(
    "This is The Number is greater than 50 "
)

prompt1=ChatPromptTemplate.from_template(
    "Number is 50 or less"
)


chain=RunnableSequence(prompt|model|parser)

def check(data):
    if data["number"]>50:
        return True
    else :
        return False


brach_chain=RunnableBranch(
    (
        check,
        prompt
    ),
    prompt1

)


res=brach_chain.invoke({
    "number":10
})
print(res)