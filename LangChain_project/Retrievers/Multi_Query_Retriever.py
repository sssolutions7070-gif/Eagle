import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_classic.retrievers.multi_query import MultiQueryRetriever

p1 = "Python is used for programming, automation, and AI." 
p2 = "Docker is used to create and manage containers." 
p3 = "MongoDB is a NoSQL database used in MERN applications." 
p4 = "React is a JavaScript library used to build user interfaces."


model=GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

alldata=[p1,p2,p3,p4]

allids=["python","Docker","MongoDB","React"]

vector_store=Chroma(
    embedding_function=model,
    persist_directory="demo_db"
)

database=vector_store.add_texts(texts=alldata,ids=allids)


base_retriver=vector_store.as_retriever(
    search_kwargs={"k":2}
)

llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

retriver=MultiQueryRetriever.from_llm(
    retriever=base_retriver,
    llm=llm
)

query="Which datbase is used in the Mern Applications"

res=retriver.invoke(query)
for i in res:
    print(i.page_content)


