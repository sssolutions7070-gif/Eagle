import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence


model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

detailed_promt=PromptTemplate.from_template(
    "write a proper profitional one line title for blog where topic is {topic}"
)

detailed_promt1=PromptTemplate.from_template(
    "write a proper profitional summary for blog where topic is {title}"
)
parser=StrOutputParser()

chain=RunnableSequence(detailed_promt,model,parser)
chain1=RunnableSequence(detailed_promt1,model,parser)


title=chain.invoke({
    "topic":"PM Of india"
})

print("Title:")
print(title)

summary=chain1.invoke({
    "title":title
})



print("Summary:")
print(summary)