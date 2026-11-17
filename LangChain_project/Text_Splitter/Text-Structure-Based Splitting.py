from langchain_text_splitters import RecursiveCharacterTextSplitter

text="""
Python is a programming language.
It is easy to learn. 
Python is used in web development. 
Python is also used in AI and data science. 
"""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks=splitter.split_text(text)

for chunk in chunks:
    print(chunk)
   


