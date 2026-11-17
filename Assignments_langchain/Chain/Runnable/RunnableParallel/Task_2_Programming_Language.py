import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 2: Programming Language
• Input: Programming language  
• Generate at the same time:  
o Definition  
o 3 features  
o One use  

"""

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableSequence
from langchain_core.output_parsers import StrOutputParser

parser=StrOutputParser()


model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)
prompt1=PromptTemplate.from_template(
    "Genrate a defination as per the {topic}"

)

prompt2=PromptTemplate.from_template(
    "Genarate 3 features as per the {topic}"
)
prompt3=PromptTemplate.from_template(
    "give me the use of that as per the {topic}"
)
topic=input("Enter the Topic")
defination_chain=RunnableSequence(prompt1,model,parser)
three_features_chain=RunnableSequence(prompt2,model,parser)
use_chain=RunnableSequence(prompt3,model,parser)

parallel_chain=RunnableParallel({
    "defination":defination_chain,
    "three_feacture":three_features_chain,
    "use":use_chain

}
)

res=parallel_chain.invoke({
    "topic":topic
})

print("defination",res["defination"])
print("three_feacture",res["three_feacture"])
print("use",res["use"])


