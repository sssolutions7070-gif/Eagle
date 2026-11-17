from langchain_community.document_loaders import CSVLoader

loader=CSVLoader("LangChain_project/RAG_Loaders/students.csv")

documets=loader.load()

print(documets)

