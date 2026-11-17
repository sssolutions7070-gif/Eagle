"""
4. Multiple Pages 
• Take a PDF having at least 5 pages. 

• Load it using PyPDFLoader. 
• Print the content of every page using a loop. 

"""

from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("Assignments_langchain/RAG_Loaders/Py_PDF_Loader/5. RAG in LangChain (2).pdf")

document=loader.load()

print("Total pages:", len(document))
i=0

for page in document:
    if i < len(document):
        print(document[i].page_content)
        i=i+1


#Website_Content.py 

