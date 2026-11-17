from langchain_core.tools import StructuredTool
from pydantic import BaseModel


class attendence_input(BaseModel):
    att:int


def attence_check(att:int) -> str:
    "this is attance chck system"
    if att>=75:
        return "Elligible"
    else:
        return "Not Elligible"

attendence_tool=StructuredTool.from_function(
    func=attence_check,
    name="attence_check",
    description="this is attance chck system",
    args_schema=attendence_input
)

res=attendence_tool.invoke({"att":78})

print(res)