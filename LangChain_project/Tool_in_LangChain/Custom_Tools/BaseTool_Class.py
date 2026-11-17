from langchain_core.tools import BaseTool

class AttendenceTool(BaseTool):
    name:str ="attendence chck",
    description:str="chcek atendence check"

    def _run(self,att:int) -> str:
        if att>=75:
            return "elligible"
        else:
            return "not elligible"

attendence_tool=AttendenceTool()


res=attendence_tool.invoke({"att":76})
print(res)