import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.retrievers import MultiQueryRetriever


model=GoogleGenerativeAIEmbeddings(
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    model = "models/gemini-embedding-001"
)


p1 = "Python is used for programming, automation, and AI." 
p2 = "Docker is used to create and manage containers." 
p3 = "MongoDB is a NoSQL database used in MERN applications." 
p4 = "React is a JavaScript library used to build user interfaces."

alldata=[p1,p2,p3,p4]
allids=["Python1","Docker1","Mongo1","React1"]

vector_store=Chroma(
    embedding_function=model,
    persist_directory="demo_db",
    collection_name="retrive_collection"
)

database=vector_store.add_texts(texts=alldata,ids=allids)

base_retriever=vector_store.as_retriever(
    search_kwargs={"k":2}
)


llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

retriever=MultiQueryRetriever.from_llm(
    retriever=base_retriever,
    llm=llm
)

query="which database is used in the Mearn Stack"

res=retriever.invoke(query)
print(res[0].page_content)