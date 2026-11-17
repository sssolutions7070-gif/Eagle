"""
7. Student CSV 
• Create students.csv with columns: o name o age o branch o marks • Add at least 5 students. 
• Load it using CSVLoader. 
• Print every student's document

"""
from langchain_community.document_loaders import CSVLoader


loader=CSVLoader("Assignments_langchain/RAG_Loaders/CSV_Loader/students (2).csv")

documet=loader.load()



print(documet)


#Product_CSV.py
