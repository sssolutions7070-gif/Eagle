import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


model=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

Country=input("Enter Any Country")

prompt=PromptTemplate(
    template="who is pm of {Country}",
    input_variables=["Country"]
)

complete=prompt.invoke({"Country":Country})

ans=model.invoke(complete)
print(ans.text)



