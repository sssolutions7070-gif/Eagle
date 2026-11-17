import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 4: Exam Preparation Assistant (PDF + TXT) 
Create a RAG application that searches a syllabus PDF and study notes stored in a TXT file. 
Requirements: 
• Load documents in both formats. 
• Store document chunks and their metadata. 
• Retrieve relevant information from both sources. 
• Answer questions and generate practice questions based on the retrieved content. 
Sample Query: "Explain deadlock and generate five practice questions from my study 
notes." 

"""

from langchain_community.document_loaders import PyPDFLoader,TextLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

pdf_loader=PyPDFLoader("Assignments_langchain/RAG_and_AI_Agent/operating_systems_syllabus.pdf")

pdf_documents=pdf_loader.load()

print("PDF Loded succesfully length of pdf is",len(pdf_documents),"pages(o)")

txt_loader=TextLoader("Assignments_langchain/RAG_and_AI_Agent/operating_systems_study_notes.txt")

txt_documents=txt_loader.load()

print("text file loaded succesfully length of text file is",len(txt_documents),"pages(o)")

for doc in pdf_documents:
    doc.metadata["source_type"]="pdf"

for doc in txt_documents:
    doc.metadata["source_type"]="txt"

documents=pdf_documents+txt_documents

print("now this is the total documents total documents length is",len(documents))

llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

splitter=RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks=splitter.split_documents(documents)
print("chunks",chunks)
embeddings=GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

vector_store=Chroma.from_documents(
    documents=chunks,
    embedding=embeddings
)

retiver=vector_store.as_retriever(
    search_kwargs={"k":6}
)

question = (
    "Explain deadlock and generate five practice "
    "questions from my study notes."
)

doc_retiver=retiver.invoke(question)

context="\n\n".join(
    doc.page_content for doc in doc_retiver
)

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
    "question":question
})

print("final oputput")
print(response.text)