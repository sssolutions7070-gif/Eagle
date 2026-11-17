import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

parser=StrOutputParser()

title_prompt=ChatPromptTemplate.from_template(
    "Create an attractive and professional title about {topic}"
)

title_chain=title_prompt | model | parser
keyword_prompt=ChatPromptTemplate.from_template(
    "Generate 5 important keywords related to {topic}"
)

keyword_chain=keyword_prompt | model | parser

descriptive_prompt=ChatPromptTemplate.from_template(
    "Write a short and professional description about {topic}"
)
descriptive_chain= descriptive_prompt | model | parser

parallel_chain= RunnableParallel(
    title=title_chain,
    keyword=keyword_chain,
    descriptive=descriptive_chain
)

topic=input("Enter Topic:")

result=parallel_chain.invoke({
    "topic":topic
})

print("\n==============================") 
print("TITLE") 
print("==============================") 
print(result["title"])

print("\n==============================") 
print("KEYWORDS")
print("==============================")
print(result["keyword"])

print("\n==============================")
print("DESCRIPTION")
print("==============================")
print(result["descriptive"])