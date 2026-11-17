"""
5. Website Content 
• Choose any educational website. 
• Use WebBaseLoader to load the website. 
• Print the extracted page_content. 

"""


from langchain_community.document_loaders import WebBaseLoader

loader=WebBaseLoader(
    "https://play.google.com/store/apps/details?id=in.bestfoodservices.delivery"
)

document=loader.load()

print(document)


