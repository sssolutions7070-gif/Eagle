from langchain_text_splitters import MarkdownHeaderTextSplitter 


text = """
# Python

Python is a programming language.

## Features

Python is easy to learn.

### Applications

Python is used in AI and web development.
"""

headers_to_split_on=[
    ("#","Heading 1"),
    ("##","Heading 2"),
    ("###","Heading 3"),
    
    
]

splitters=MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

documents=splitters.split_text(text)

for doc in documents:
    print("Content",doc.page_content)
    print("MetaData",doc.metadata)
    print("=====================")


    