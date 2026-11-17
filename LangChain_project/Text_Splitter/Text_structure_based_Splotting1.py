from langchain_text_splitters import RecursiveCharacterTextSplitter

text="""
Python is a programming language.  
Python is easy to learn and widely used.
Python is used in AI, web development and data science. 

"""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks=splitter.split_text(text)

for chunk in chunks:
    print(chunk)


