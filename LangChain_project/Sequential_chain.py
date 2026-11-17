import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

parser=StrOutputParser()

prompt1=ChatPromptTemplate.from_template(
    "Create an attractive and professional blog title about {topic}" 
)

blog_title= prompt1 | model | parser

prompt2=ChatPromptTemplate.from_template(
    """Write a proper, professional and attractive blog
    based on the following title:
    {title}    
    """ 
)

blog_content=prompt2 | model | parser

prompt3=ChatPromptTemplate.from_template(
    """Write a proper and interesting summary
    of the following blog: 
    {blog_content}    
    """
)
blog_summary=prompt3 | model | parser 

topic=input("Enter Topic Here")

title=blog_title.invoke({
    "topic":topic
})

content=blog_content.invoke({
    "title":title
})

summary=blog_summary.invoke({
    "blog_content":content
})

print("\n==============================") 
print("BLOG TITLE") 
print("==============================") 
print(title)  
print("\n==============================") 
print("BLOG CONTENT") 
print("==============================") 
print(content)  
print("\n==============================") 
print("BLOG SUMMARY") 
print("==============================") 
print(summary) 