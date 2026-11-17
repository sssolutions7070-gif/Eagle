import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 1: Country 
• Input: Country name  
• Generate at the same time:  
o Capital  
o Population  
o One famous place 

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
    "Generate  Capital of {country_name}"
)
prompt2=PromptTemplate.from_template(
    "Generate the counnt of  Population {country_name} "
)
prompt3=PromptTemplate.from_template(
    "One famous place {country_name}"
)
country_name=input("please enter country name")

capital_prompt=RunnableSequence(prompt1,model,parser)
population_prompt=RunnableSequence(prompt2,model,parser)
place_prompt=RunnableSequence(prompt3,model,parser)





parallel_chain=RunnableParallel({
    "capital":capital_prompt,
    "population":population_prompt,
    "place":place_prompt
    
})

res=parallel_chain.invoke({
    "country_name":country_name
})


print("\nCapital:", res["capital"])
print("Population:", res["population"])
print("Famous Place:", res["place"])