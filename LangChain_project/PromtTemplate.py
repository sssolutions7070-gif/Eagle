import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

Country=input("Enter Your Contry:")


prompt=PromptTemplate(
    template="Who is PM of{Country}",
    input_variables=["Country"]
)

complete_prompt=prompt.invoke({"Country":Country})

ans=model.invoke(complete_prompt)
print(ans.text)