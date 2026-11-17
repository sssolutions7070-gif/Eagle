import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

model=GoogleGenerativeAIEmbeddings(
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    model = "models/gemini-embedding-001"
)

doc1 = "Python is programming language use in Ai development" 

doc2 = "react is web framework use in web development" 

doc3 = "java is programming language use in backend development" 

alldocs=[doc1,doc2,doc3]

vector_store=Chroma(
    embedding_function=model,
    persist_directory="demo_db",
    collection_name="collection_name"
)

allids=["python1","react1","java1"]

database=vector_store.add_texts(texts=alldocs,ids=alldocs)

embeddingdata=vector_store.get(include=["embeddings"])

print(embeddingdata)

res=vector_store.similarity_search(
    query="web devlopment"
)

print(res[0].page_content)