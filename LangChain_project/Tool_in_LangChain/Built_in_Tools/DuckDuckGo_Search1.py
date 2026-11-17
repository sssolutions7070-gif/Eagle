from langchain_community.tools import DuckDuckGoSearchResults 

res=DuckDuckGoSearchResults()

res1=res.invoke("who is pm of india")

print(res1)

