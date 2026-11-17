import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

embeddings=GoogleGenerativeAIEmbeddings(
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    model = "models/gemini-embedding-001"
)

splitter=SemanticChunker(embeddings)

text="""
Python is a programming language. 
Python is easy to learn. 
Python is widely used in software development.  
The stock market changes every day. 
Investors buy and sell shares. 
Stock prices can increase or decrease. 
"""

documents=splitter.create_documents([text])

for doc in documents:
    print(doc.page_content)