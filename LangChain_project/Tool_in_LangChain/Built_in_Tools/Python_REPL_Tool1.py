from langchain_experimental.tools import PythonAstREPLTool

res=PythonAstREPLTool()

res1=res.invoke(
    "print(10+20)"
)

print(res1)


