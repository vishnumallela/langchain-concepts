import os
import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
dotenv.load_dotenv("/Users/vishnumallela/Documents/Learning/LangChain/py.env")

# Initialize model and parser
model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))
parser = StrOutputParser()

# Create a chain using pipe operator
chain = model | parser

# Invoke the chain and print the result
result = chain.invoke("Hello LLM")
print(result)