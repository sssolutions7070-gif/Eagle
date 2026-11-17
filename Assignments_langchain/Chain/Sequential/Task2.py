import os
from dotenv import load_dotenv
load_dotenv()

"""
2. Blog Generator 
• Take a topic as input. 
• Generate a blog title.
• Generate blog content based on the title. 
• Generate a short summary of the blog. 

"""

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

parser=StrOutputParser()

prompt1=PromptTemplate.from_template(
    "please genarte a title of this blog using this topic{topic}"
)

blog_title=prompt1 | model | parser

prompt2=PromptTemplate.from_template(
    "Generate blog content based on the title{blog_title}"
)

blog_content= prompt2 | model | parser

prompt3=PromptTemplate.from_template(
    "Generate a short summary of the blog uisng the blog content{blog_content}"
)
blog_summary=prompt3 | model | parser

topic=input("Enter the TOpic")

title=blog_title.invoke({
    "topic":topic
})

content=blog_content.invoke({
    "blog_title":title
})

summary=blog_summary.invoke({
    "blog_content":content
})


print("===========================")
print("title")
print(title)
print("===========================")
print("Content")
print(content)
print("====================")
print("SUMMARY")
print(summary)
print("=======================")