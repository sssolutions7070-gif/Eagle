"""
Create college_rules.txt. 
Add at least 10 college rules.
Load the file using TextLoader.
Print each loaded document's content. 

"""

from langchain_community.document_loaders import TextLoader


loader=TextLoader("Assignments_langchain/RAG_Loaders/Text_Loader/rules.txt")

document=loader.load()

print(document[0].page_content)
print(document)