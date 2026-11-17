from langchain_community.document_loaders import PyPDFLoader


loader=PyPDFLoader("LangChain_project/RAG_Loaders/Satej_Rajeshirke_Resume (17).pdf")

documents=loader.load()

print(documents)