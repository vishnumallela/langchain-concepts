from dotenv import load_dotenv
import os
from langfuse import Langfuse
from langfuse.decorators import observe
from langfuse.openai import openai

# Load environment variables
load_dotenv("/Users/vishnumallela/Documents/Learning/LangChain/py.env")

# Initialize Langfuse
langfuse = Langfuse(
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    host="https://cloud.langfuse.com"
)

@observe()
def story():
    return openai.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=[
            {"role": "system", "content": "You are a great storyteller."},
            {"role": "user", "content": "Once upon a time in a galaxy far, far away..."}
        ],
    ).choices[0].message.content

@observe()
def main():
    return story()

# Execute main function
main()