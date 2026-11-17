import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 2: Company Policy Assistant (Word Document) 
Create a RAG application that answers employee questions using a company policy 
document in DOCX format. 
Requirements: 
• Load a Word document. 
• Split and embed the document content.
• Retrieve relevant policy information.
• Answer questions based on the document and indicate when information is
unavailable.
Sample Query: "How many days of annual leave can an employee take?"

"""

from langchain_community.document_loaders import Docx2txtLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

loaders=Docx2txtLoader("Assignments_langchain/RAG_and_AI_Agent/company_policy_demo.docx")

document=loaders.load()

print("len of documet",len(document),"pages(o)")

llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

splitter=RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks=splitter.split_documents(document)

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
question="How many days of annual leave can an employee take?"
doc_retiver=retiver.invoke(question)

context="\n\n".join(
    doc.page_content for doc in doc_retiver
)

print("data is retrived now")

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

response1=chain.invoke({
    "context":context,
    "question":question
})


print("final output")
print(response1.text)
