import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv("/Users/vishnumallela/Documents/Learning/LangChain/py.env")

# Initialize LLM (OpenAI)
llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))

# Invoke LLM
response = llm.invoke("Hello, world!")
print("Response Object:", response)
print("Response Content:", response.content)

# Printing the response content with in-built output parser
parser = StrOutputParser()
parsed_response = parser.invoke(response)
print("Response Content Object parsed with StrOutputParser:", parsed_response)

# Linking model to a parser (chaining)
chain = llm | parser
chained_response = chain.invoke("Hey, what's today?")
print("Chained Response:", chained_response)


exit()