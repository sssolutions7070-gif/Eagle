from langchain_core.tools import BaseTool



class Attendece_strct(BaseTool):
    name:str ="attanedence chck"
    description:str ="chcks the attandence "

    def _run(self,att:int) -> str:
        if att>75:
            return "elligible"
        else:
            return "not elligible"

attendec_tool=Attendece_strct()
res=attendec_tool.invoke({"att":78})
print(res)