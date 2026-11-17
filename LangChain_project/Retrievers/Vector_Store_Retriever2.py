import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

model=GoogleGenerativeAIEmbeddings(
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    model = "models/gemini-embedding-001"
)

p1 = "Python is used for programming, automation, and AI." 
p2 = "Docker is used to create and manage containers." 
p3 = "MongoDB is a NoSQL database used in MERN applications." 
p4 = p4 = "React is a JavaScript library used to build user interfaces." 

alldata=[p1,p2,p3,p4]

allids=["Python","Docker","MongoDB","React"]

vector_store=Chroma(
    embedding_function=model,
    persist_directory="demo_db",
    collection_name="Vect_collection"
)
database=vector_store.add_texts(texts=alldata,ids=allids)

retriver=vector_store.as_retriever(
    search_kwargs={"k":1}
)


query="which databse is used for MERN Stack?"

res=retriver.invoke(query)

print(res[0].page_content)