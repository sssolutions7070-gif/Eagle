from langchain_community.tools import DuckDuckGoSearchRun

search=DuckDuckGoSearchRun()

res=search.invoke("What is artificial intelligence?")
print(res)