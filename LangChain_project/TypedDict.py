from typing  import TypedDict

class person(TypedDict):
    name:str
    age:int
    contact:str


info:person={
    "name":"satej",
    "age":30,
    "contact":"9156994716"
}

print(info)