from langchain_core.tools import StructuredTool
from pydantic import BaseModel

class attendence_strcuct(BaseModel):
    att:int

def attendence_check(att:int) -> str:
    if att>=75:
        return "elligible"
    else:
        return "Not Elligible"

attendence_tool=StructuredTool.from_function(
    func=attendence_check,
    name="attendence_check",
    description="this is attanedence tool",
    args_schema=attendence_strcuct
)

res=attendence_tool.invoke({"att":78})
print(res)