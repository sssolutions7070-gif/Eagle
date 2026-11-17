import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

# Create the Groq model
model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

# Store conversation history
messages = []

while True:

    question = input("You: ")

    # Exit condition
    if question.lower() == "exit":
        print("Chat ended.")
        break

    # Add user's question to history
    messages.append(HumanMessage(content=question))

    # Send complete conversation history to the model
    answer = model.invoke(messages)

    # Print AI response
    print("AI:", answer.content)

    # Add AI response to history
    messages.append(AIMessage(content=answer.content))
