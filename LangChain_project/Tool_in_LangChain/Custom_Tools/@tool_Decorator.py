from langchain_core.tools import tool


@tool
def attendence_check(attendence:int) -> str:
    """THis is Attendence Checkar system"""
    if attendence>=75:
        return "Elligible"
    else:
        return "Not Elligible"

res=attendence_check.invoke({"attendence":78})

print(res)


