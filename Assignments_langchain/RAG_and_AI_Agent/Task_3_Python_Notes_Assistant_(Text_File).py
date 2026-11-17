import os
from dotenv import load_dotenv
load_dotenv()

"""
Task 3: Python Notes Assistant (Text File) 
Create a RAG application that explains programming concepts using a Python notes text 
file. 
Requirements: 
• Load a TXT file containing Python notes. 
• Create text chunks and embeddings. 
• Retrieve relevant notes. 
• Generate simple explanations based on the retrieved content. 
Sample Query: "Explain Python lists and tuples based on my notes."
"""

from langchain_community.document_loaders import TextLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

loaders=TextLoader("Assignments_langchain/RAG_and_AI_Agent/python_notes.txt")

documents=loaders.load()

print("length Documents",len(documents),"pages(o)")

llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

splitter=RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks=splitter.split_documents(documents)

print("Chunks",chunks)

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

question="Explain Python lists and tuples based on my notes."

retiver_doc=retiver.invoke(question)
context="\n\n".join(
    doc.page_content for doc in retiver_doc
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

chain= prompt | llm

response=chain.invoke({
    "context":context,
    "question":question
})

print("final output")
print(response.text)