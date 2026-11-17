"""
1. Student Information 
• Create students.txt. 
• Add information about 5 students. 
• Use TextLoader to load the file. 
• Print the complete text using page_content. 

"""
from langchain_community.document_loaders import TextLoader

loader=TextLoader("Assignments_langchain/RAG_Loaders/Text_Loader/demo.txt")

document=loader.load()

print(document)

print(document[0].page_content)