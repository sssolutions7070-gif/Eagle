import os
from dotenv import load_dotenv
load_dotenv()

"""
1. Story Generator • 
Take a story topic as input. 
• Generate a story title. 
• Generate a story based on the title. 
• Generate a short summary of the story. 

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
    """
    Generate a creative and interesting title for a story
    based on the following topic:{topic}Return only the title.
    """
)

story_topic=prompt1 | model | parser

prompt2=PromptTemplate.from_template(
    """Write a short and engaging story based on the following title: {story_topic} The story should have a clear beginning, middle, and ending."""
)

story_title=prompt2 | model | parser

prompt3=PromptTemplate.from_template(
    """
    Generate a short summary of the following story:

    Story:
    {story_title}

    Return only the summary.
    """
)

story_summary=prompt3 | model | parser

topic=input("Please enter the story topic")

# Generate title
title = story_topic.invoke({
    "topic": topic
})

# Generate story
story = story_title.invoke({
    "story_topic": title
})

# Generate summary
summary = story_summary.invoke({
    "story_title": story
})

print("======================================")
print("TITLE")
print(topic)
print("=====================================")
print("TITLE")
print(title)
print("======================================")
print("SUMMARY")
print(summary)
print("======================================")