import os
from dotenv import load_dotenv
load_dotenv()

"""


Task 13: Job Application Assistant Agent 
Create an AI agent that checks a resume against a job description. 
Tools: 
1. CountResumeWords(resume_text) — counts the words in a resume. 
2. FindRequiredSkills(resume_text, required_skills) — identifies required skills 
mentioned in the resume. 
3. CheckResumeLength(word_count, minimum_words) — checks whether the resume 
meets a defined word-count target. 
Sample Query: "Check my resume for Python, SQL, and React skills. Count the words and 
tell me whether it meets a 200-word target."
"""

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

@tool
def count_resume_words(resume_text: str) -> str:
    """Count the number of words in the resume."""
    word_count = len(resume_text.split())
    return f"Resume word count = {word_count}"


@tool
def find_required_skills(
    resume_text: str,
    required_skills: list[str]
) -> str:
    """Find which required skills are mentioned in the resume."""
    found = []
    missing = []

    for skill in required_skills:
        if skill.lower() in resume_text.lower():
            found.append(skill)
        else:
            missing.append(skill)

    return f"Skills found: {found}. Skills missing: {missing}."

@tool
def check_resume_length(word_count: int, minimum_words: int) -> str:
    """Check whether the resume meets the minimum word count."""
    if word_count >= minimum_words:
        return f"Resume meets the {minimum_words}-word target."
    else:
        return (
            f"Resume does not meet the target. "
            f"Add {minimum_words - word_count} more words."
        )


tools=[count_resume_words,find_required_skills,check_resume_length]
llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

llm_with_model=llm.bind_tools(tools)
# Sample query
# Sample resume
resume_text = """
I am a software developer with knowledge of Python,
SQL, HTML, CSS, JavaScript, and React.
I have developed web applications and worked with databases.
I enjoy solving problems and learning new technologies.
"""

question = f"""
Check this resume for a job application.

Resume:
{resume_text}

Required skills: Python, SQL, React.
Minimum word target: 200 words.

1. Count the resume words.
2. Find the required skills in the resume.
3. Check whether the resume meets the 200-word target.
"""
res = llm_with_model.invoke(question)
print(res.tool_calls)


for i in res.tool_calls:
    if i["name"]=="count_resume_words":
        result=count_resume_words.invoke(i["args"])
    elif i["name"]=="find_required_skills":
        result=find_required_skills.invoke(i["args"])
    elif i["name"]=="check_resume_length":
        result=check_resume_length.invoke(i["args"])

    print(i["name"],":",result)









    