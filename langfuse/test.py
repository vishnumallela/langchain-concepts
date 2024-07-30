import os
from dotenv import load_dotenv
from langfuse import Langfuse
from langfuse.decorators import observe, langfuse_context
from langfuse.openai import openai

# Load environment variables
load_dotenv("/Users/vishnumallela/Documents/Learning/LangChain/py.env")

# Initialize Langfuse
langfuse = Langfuse(
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    host=os.getenv("LANGFUSE_HOST"),
)

@observe()
def generate_story():
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=[
            {"role": "system", "content": "You are a great storyteller."},
            {"role": "user", "content": "Once upon a time in a galaxy far, far away..."}
        ],
    )
    
    langfuse_context.update_current_trace(
        metadata={
            "groupId": "1234567890",
            "sessionId": "1234567890",
            "historyId": "9876543210"
        }
    )
    
    return response.choices[0].message.content

@observe()
def main():
    return generate_story()

if __name__ == "__main__":
    print(main())