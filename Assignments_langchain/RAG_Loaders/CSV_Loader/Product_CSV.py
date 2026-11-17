"""
Product CSV 
• Create products.csv with: o product_name o price o category o stock 
• Add at least 10 products. 
• Load the CSV and print the page_content of each document.

"""

from langchain_community.document_loaders import CSVLoader
loader=CSVLoader("Assignments_langchain/RAG_Loaders/CSV_Loader/products.csv")

document=loader.load()

print(document)
