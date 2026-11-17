import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 5: Business Document Research Assistant (PDF + DOCX + TXT) 
Create a RAG application that answers questions by searching multiple business 
documents. 
Requirements: 
• Load PDF, DOCX, and TXT files. 
• Split documents and generate embeddings. 
• Retrieve relevant content across documents. 
• Include source document names in answers. 
• Compare information found in different documents. 
Sample Query: "Compare the product features mentioned in the product manual and 
company proposal."
"""

from langchain_community.document_loaders import PyPDFLoader,TextLoader,Docx2txtLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

pdf_loader=PyPDFLoader("Assignments_langchain/RAG_and_AI_Agent/product_manual.pdf")

pdf_documents=pdf_loader.load()

print("PDF Loded succesfully length of pdf is",len(pdf_documents),"pages(o)")

txt_loader=TextLoader("Assignments_langchain/RAG_and_AI_Agent/business_notes.txt")

txt_documents=txt_loader.load()

docx_loader=Docx2txtLoader("Assignments_langchain/RAG_and_AI_Agent/company_proposal.docx")
docx_documents=docx_loader.load()


print("text file loaded succesfully length of text file is",len(txt_documents),"pages(o)")

for doc in pdf_documents:
    doc.metadata["source_type"]="pdf"

for doc in txt_documents:
    doc.metadata["source_type"]="txt"
for doc in docx_documents:
    doc.metadata["source_type"]="docx"
    
documents=pdf_documents+txt_documents+docx_documents

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

question = "Compare the product features mentioned in the product manual and company proposal."

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