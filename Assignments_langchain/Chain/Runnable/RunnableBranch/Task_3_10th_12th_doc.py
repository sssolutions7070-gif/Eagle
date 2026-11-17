import os
from dotenv import load_dotenv
load_dotenv()

"please enter the inputs there like 10th and 12 th and showing there 10 th documents and the 12th "
"documtes for the admminsion in that the input choosssing there 10th and 12 there "


from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch


model=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)


parser = StrOutputParser()


prompt1 = ChatPromptTemplate.from_template(
    """
    10th Admission Documents:

    1. 10th Marksheet
    2. 10th Passing Certificate
    3. School Leaving Certificate
    """
)


prompt2 = ChatPromptTemplate.from_template(
    """
    12th Admission Documents:

    1. 12th Marksheet
    2. 12th Passing Certificate
    3. School Leaving Certificate
    """
)


def check(data):
    if data["education"] == "10th":
        return True
    else:
        return False


branch_chain = RunnableBranch(
    (check, prompt1),
    prompt2
)


education = input(
    "Enter Your Education | Please use 10th or 12th: "
)


res = branch_chain.invoke({
    "education": education
})


print(res)