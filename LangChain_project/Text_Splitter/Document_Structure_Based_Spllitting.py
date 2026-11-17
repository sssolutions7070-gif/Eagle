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
    ("#","header1"),
    ("##","header 2"),
    ("###","header 3")
]

splitter=MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)


docu=splitter.split_text(text)


for doc in docu:
    print("content:",doc.page_content)
    print("markdown:",doc.metadata)