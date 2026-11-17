import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

loaders=PyPDFLoader("Assignments_langchain/RAG_and_AI_Agent/clg_rules.pdf")

documents=loaders.load()


print("length of pdf is",len(documents),"pages(s)")

splitter=RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks=splitter.split_documents(documents)

print("total chunks:",chunks)

embeddings=GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

vector_store=Chroma.from_documents(
    documents=chunks,
    embedding=embeddings
)

print("Documenst stored in vecor database")

retiver=vector_store.as_retriever(
    search_kwargs={"k":6}
)

question="what is minimum attendence required?"

relevent_docs=retiver.invoke(question)

context="\n\n".join(
    doc.page_content for doc in relevent_docs
)

print("\n Retrived Context:")

prompt=ChatPromptTemplate.from_messages([
    (
        "system", 
        """Answer the question using only the provided context. 
        If the answer is not in the context, say: 
        'The information is not available in the document.'""" 
    ),
    (
        "human", 
        "Context:\n{context}\n\nQuestion: {question}"
    )
])

chain=prompt | llm

respose=chain.invoke({
    "context":context,
    "question":question
})

print("\n Final OutPut")
print(respose.text)