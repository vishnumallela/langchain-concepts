import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv("/Users/vishnumallela/Documents/Learning/LangChain/py.env")

# Initialize the model and parser
model = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))
parser = StrOutputParser()

# Get user input
human_input = input("Enter a math equation: ")

# Prepare messages
messages = [
    # System-Message: Provides context to the LLM to ensure it understands the user's intent
    SystemMessage(content="You are a helpful math assistant that calculates simple math problems for the user. Your name is Vishnu."),
    
    # Human-Message: This is given by the user
    HumanMessage(content=human_input)
]

# Create the chain and get the response
chain = model | parser
response = chain.invoke(messages)

# Print the response
print("Response from the model using Human and System Messaging:", response)

exit()
