import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableSequence,
    RunnablePassthrough,
    RunnableBranch,
    RunnableLambda
)


# Model
model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

# Prompt 1 - Blog
prompt1 = ChatPromptTemplate.from_template(
    "Write a proper, simple and short blog on {topic}"
)


# Prompt 2 - Summary
prompt2 = ChatPromptTemplate.from_template(
    "Write a short summary of this blog:\n{content}"
)


# Parser
parser = StrOutputParser()


# Blog generation chain
chain = RunnableSequence(
    prompt1,
    model,
    parser
)


# Summary chain
summary_chain = RunnableSequence(
    prompt2,
    model,
    parser
)


# Condition
def check_blog(blog):

    if len(blog.split()) > 500:
        return True
    else:
        return False


# Branch chain
branch_chain = RunnableBranch(
    (
        check_blog,
        RunnableSequence(
            RunnableLambda(
                lambda blog: {"content": blog}
            ),
            summary_chain
        )
    ),
    RunnablePassthrough()
)


# Final chain
final_chain = RunnableSequence(
    chain,
    branch_chain
)


# Invoke
res = final_chain.invoke({
    "topic": "PM of India"
})


# Output
print(res)