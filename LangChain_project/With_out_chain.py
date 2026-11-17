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

topic=input("Enter Topic Here:")

prompt1=ChatPromptTemplate.from_template(
    "Create the attractive and proffectional blog about{topic}"
)

detail_prompt=prompt1.invoke({
    "topic":topic
})

response=model.invoke(detail_prompt)

blog_content=parser.invoke(response)

#step2

prompt2=ChatPromptTemplate.from_template(
    "create a short and simple 5 line summary of {blog_content}"
)

detailed_prompt2=prompt2.invoke({
    "blog_content":blog_content
})

summary_content=model.invoke(detailed_prompt2)

summary=parser.invoke(summary_content)

print("==========================")
print("BLOG")
print(blog_content)
print("==========================")
print("\n========================")
print("SUMMARY")
print(summary)
print("\n===========================")


