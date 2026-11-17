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

alldata=[doc1,doc2,doc3]

vector_store=Chroma(
    embedding_function=model,
    persist_directory="demo_db",
    collection_name="demo_collection"
)

allids=["python1","react1","java1"]


database=vector_store.add_texts(texts=alldata,ids=allids)
print(database)

documents=vector_store.get(include=["embeddings"])

print(documents)

res=vector_store.similarity_search(
    query="web development"
)
print(res[0].page_content)