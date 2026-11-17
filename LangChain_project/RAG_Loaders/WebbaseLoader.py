from langchain_community.document_loaders import WebBaseLoader


loader=WebBaseLoader(
    "https://play.google.com/store/apps/details?id=in.bestfoodservices.delivery"
)

documents=loader.load()

print(documents)

print(documents[0].page_content)