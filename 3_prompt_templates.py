import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env file
load_dotenv("/Users/vishnumallela/Documents/Learning/LangChain/py.env")

# Define user and system message templates
user_template = "{input}"
system_template = "Translate the following into {language}:"

# Create a ChatPromptTemplate from the message templates
prompt_template = ChatPromptTemplate.from_messages([
    ("user", user_template),
    ("system", system_template)
])

# Test the prompt template with sample input
messages = prompt_template.invoke({"language": "French", "input": "Hello"})
print(messages)

# Initialize the OpenAI model with the API key from environment variables
model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))

# Initialize the output parser
parser = StrOutputParser()

# Chain the prompt template, model, and parser together
chain = prompt_template | model | parser

# Test the entire chain with sample input
result = chain.invoke({"language": "French", "input": "Hello"})
print(result)