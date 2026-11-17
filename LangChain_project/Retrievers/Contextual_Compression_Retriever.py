import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from langchain_chroma import Chroma 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor

# 1. Create four paragraphs 
p1 = "Python is used for programming, automation, and AI." 
p2 = "Docker is used to create and manage containers." 
p3 = "MongoDB is a NoSQL database used in MERN applications." 
p4 = "React is a JavaScript library used to build user interfaces."  

model=GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

alldata=[p1,p2,p3,p4]

allids=["python","docker","mongobd","react"]


vector_store=Chroma(
    embedding_function=model,
    persist_directory="demo_db",
    collection_name="demo_collectiom"
)

database=vector_store.add_texts(texts=alldata,ids=allids)

base_retriever=vector_store.as_retriever(
    search_kwars={"k":2}
)


llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

compresser=LLMChainExtractor.from_llm(llm)

retriver=ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compresser
)

query="What is MongoDB used for?"

res=retriver.invoke(query)

for results in res:
    print(results.page_content)