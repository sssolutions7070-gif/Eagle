from langchain_text_splitters import CharacterTextSplitter

text =""" 
Python is a programming language.
It is easy to learn. Python is used in web development.
Python is also used in AI and data science. 
"""

splitter=CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0
)

chuks=splitter.split_text(text)

for chunk in chuks:
    print(chunk)
    print("-------------------------")