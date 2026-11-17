import os
from dotenv import load_dotenv
load_dotenv()

"""
3. Topic Information Generator 
• Take a topic as input. 
• Generate a definition of the topic. 
• Generate five key points about the topic. 
• Generate one real-world example of the topic. 

"""

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

parser=StrOutputParser()
prompt1=PromptTemplate.from_template(
    "Generate a definition of the topic:{topic}"
)

blog_topic=prompt1 | model | parser

prompt2=PromptTemplate.from_template(
    "Generate five key points about the topic:{topic}"
)
blog_five=prompt2 | model | parser


prompt3=PromptTemplate.from_template(
    "Generate one real-world example of the topic.{topic}"
)
blog_real=prompt3 | model | parser

parallel_chain=RunnableParallel(
    title=blog_topic,
    five=blog_five,
    real=blog_real
)

topic=input("please Enter Topic")

res=parallel_chain.invoke({
    "topic":topic

})

print("======================================")
print("Topic")
print("================")
print(res["title"])
print("==============================")
print("Five")
print(res["five"])
print("=======================")
print("real")
print(res["real"])