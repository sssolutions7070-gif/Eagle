import os
from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

model = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

llmmodel= ChatHuggingFace(llm=model)

res=llmmodel.invoke(input("Please Enter Anything Which YOU Want There?"))

print(res.content)