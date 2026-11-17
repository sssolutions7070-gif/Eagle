from langchain_text_splitters import CharacterTextSplitter

text =""" 
Python is a programming language.
It is easy to learn. Python is used in web development.
Python is also used in AI and data science. 
"""

Splitter=CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0
)

chunks=Splitter.split_text(text)
print("______________")
for chunk in chunks:
    print(chunk)
    print("________")