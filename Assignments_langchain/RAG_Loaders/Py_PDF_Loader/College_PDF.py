"""
3. College PDF 
• Take any college-related PDF. 
• Use PyPDFLoader to load it. 
• Print the content of the first page. 
"""

from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("Assignments_langchain/RAG_Loaders/Py_PDF_Loader/Satej_Rajeshirke_Resume (17).pdf")

documents=loader.load()

print(documents[0].page_content)

