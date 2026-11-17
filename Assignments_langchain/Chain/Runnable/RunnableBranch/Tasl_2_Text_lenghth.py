"""
Task 2: Text Length 
• Input: A sentence.  
• If sentence has more than 10 words → generate "Long sentence".  
• Otherwise → generate "Short sentence".  
"""


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch

parser=StrOutputParser()


prompt1=ChatPromptTemplate.from_template(
    "Long Sentence"
)

prompt2=ChatPromptTemplate.from_template(
    "Short sentence"
)
def check(sentence):
    if len(sentence)>10:
        return True
    else:
        return False

branch_chain=RunnableBranch(
    (check,
    prompt2),
    prompt1
)

res=branch_chain.invoke({
    "sentence":"This is a very long sentence which contains more than ten words"
}
)
print(res)
