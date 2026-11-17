from langchain_community.tools import tool

@tool
def Attendence_Check(Attendence:int) -> str:
    """THis is Elibible for the Voting"""
    if Attendence>=18:
        return "Elligible"
    else:
        return "Not Elligible"

res=Attendence_Check.invoke({"Attendence":10})

print(res)