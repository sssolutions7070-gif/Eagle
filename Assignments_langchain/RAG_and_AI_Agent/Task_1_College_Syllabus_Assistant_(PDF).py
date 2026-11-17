import os
from dotenv import load_dotenv
load_dotenv()

"""
Create a RAG application that answers students' questions using a college syllabus PDF. 
Requirements: 
• Load a syllabus PDF. 
• Split the document into chunks. 
• Generate embeddings and store them in a vector database. 
• Retrieve relevant information and generate answers using an LLM. 
Sample Query: "Which subjects are included in Semester 5, and how many credits does 
each subject carry?"

"""
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

loaders=PyPDFLoader("Assignments_langchain/RAG_and_AI_Agent/College_Syllabus_RAG_Application_Guide.pdf")

document=loaders.load()

print("Document length",len(document),"pages(s)")

llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

splitter=RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks=splitter.split_documents(document)

print("total Chunks",chunks)

embeddings=GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

vector_store=Chroma.from_documents(
    documents=chunks,
    embedding=embeddings
)

print("Database is Stored in the Vector Database")

retriver=vector_store.as_retriever(
    search_kwargs={"k":1}
)

question="Which subjects are included in Semester 5, and how many credits does each subject carry"

relevent_doc=retriver.invoke(question)

context="\n\n".join(
    doc.page_content for doc in relevent_doc
)

print("\n Content IS Retrived")


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


response=chain.invoke({
    "context":context,
    "queestion":question
})

print("\n final response")
print(response.text)





