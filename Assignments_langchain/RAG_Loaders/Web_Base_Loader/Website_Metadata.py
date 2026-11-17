"""
6. Website Metadata 
• Load any website using WebBaseLoader. 
• Print: o Website URL o Page title o Extracted text 

"""


from langchain_community.document_loaders import WebBaseLoader

loader=WebBaseLoader(
    "https://play.google.com/store/apps/details?id=in.bestfoodservices.delivery"
)

document=loader.load()



print(document[0].metadata.get("source"))
print(document[0].metadata.get("title"))
print(document[0].page_content)

