import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableSequence

model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)
parser=StrOutputParser()

prompt1=PromptTemplate.from_template(
    "please take a best title as per the topic:{topic}"
)

prompt2=PromptTemplate.from_template(
    "please enter the best summary as per the {topic}"
)

parallel_chain=RunnableParallel({
    "title":RunnableSequence(prompt1,model,parser),
    "summary":RunnableSequence(prompt2,model,parser)
})

res=parallel_chain.invoke({
    "topic":"pm of india"
})
print(res)