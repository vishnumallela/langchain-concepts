from langtrace_python_sdk import langtrace
from langtrace_python_sdk.utils.with_root_span import with_langtrace_root_span

from dotenv import load_dotenv
import os

load_dotenv("/Users/vishnumallela/Documents/Learning/LangChain/py.env")

from openai import OpenAI

langtrace.init(
    api_key=os.getenv("LANGTRACE_API_KEY")
)

@with_langtrace_root_span()
def example():
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "How many states of matter are there?"
            }
        ],
    )
    print(response.choices[0].message.content)

example()