import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,AIMessage


model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

message=[]

while True:

    question=input("You:")

    if question.lower()=="exit":
        print("Thank You")
        break


    message.append(HumanMessage(content=question))

    answer=model.invoke(message)

    print("AI:",answer.content)

    message.append(AIMessage(content=answer.content))






  

    