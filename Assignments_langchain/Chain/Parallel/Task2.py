import os
from dotenv import load_dotenv
load_dotenv()

"""
4. Movie Information Generator 
• Take a movie name as input. 
• Generate a short movie description. 
• Generate the main characters.
• Generate a short review of the movie. 
"""

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

parser= StrOutputParser()
model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)


prompt1=PromptTemplate.from_template(
    "Generate a short movie description{topic}"
)
movie_description=prompt1 | model | parser

prompt2=PromptTemplate.from_template(
    "Generate the main characters.{topic}"
)
movie_char=prompt2 | model | parser

prompt3=PromptTemplate.from_template(
    "Generate a short review of the movie{topic}"
)

movie_review=prompt3 | model | parser 




parallel_chain=RunnableParallel(
    description=movie_description,
    char=movie_char,
    review=movie_review
)


topic=input("please enter the input there")


res=parallel_chain.invoke({
    "topic":topic
})

print("==============================================")
print("Description")
print("==============================================")
print(res["description"])
print("==============================================")
print("Char")
print(res["char"])
print("=================================================")
print("review")
print(res["review"])
print("===================================================")