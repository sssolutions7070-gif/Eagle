from langchain_experimental.tools import PythonREPLTool


python_tool=PythonREPLTool()

res=python_tool.invoke(
    "print(10 + 20)" 
)

print(res)

