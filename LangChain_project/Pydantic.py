from pydantic import BaseModel

class person(BaseModel):
    name:str
    age:int
    mobile_no:int


info=person(
    name="Satej",
    age=30,
    mobile_no=9156994716
)


print(info)
