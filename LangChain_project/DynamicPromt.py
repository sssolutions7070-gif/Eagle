import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI


model=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

topic=input("Enter Your Topic Name:")

prompt=f"Explin {topic} in Simple language with an Example."

res=model.invoke(prompt)

print(res.text)






