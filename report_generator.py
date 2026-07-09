import os
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

from prompts import EXECUTIVE_REPORT_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

SIMPLE_PROMPT = """
You are a telecom and business expert.

Question:
{question}

Instructions:

* Answer in 2 to 5 lines.
* Keep the answer concise.
* Use simple language.
* Include one example if relevant.
* Do not generate a detailed report.
  """

def generate_report(industry, business_area, problem, objective):
    current_date = datetime.now().strftime("%B %Y")

    simple_keywords = [
        "what is",
        "define",
        "explain",
        "meaning of",
        "full form",
        "what are",
        "difference between",
        "how does"
    ]

    is_simple_question = any(
        problem.lower().startswith(keyword)
        for keyword in simple_keywords
    )

    if is_simple_question:
        prompt = SIMPLE_PROMPT.format(
        question=problem
    )
    else:
        prompt = EXECUTIVE_REPORT_PROMPT.format(
        industry=industry,
        business_area=business_area,
        problem=problem,
        objective=objective,
        current_date=current_date
    )

    response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.3,
    max_tokens=1000
)

    return response.choices[0].message.content

