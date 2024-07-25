import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from the .env file
load_dotenv("/Users/vishnumallela/Documents/Learning/LangChain/py.env")

# Initialize the OpenAI model with the API key from environment variables
model = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))

# Initialize the output parser
output_parser = StrOutputParser()

# Create a prompt template for asking the capital of a country
prompt_template = ChatPromptTemplate.from_template("What is the capital of {country}?")

# Create a chain that combines the prompt template, model, and output parser
chain = prompt_template | model | output_parser

# Invoke the chain with the input country "India" to get the capital
output_1 = chain.invoke({"country": "India"})

# Create a second prompt template for asking about the safety of the capital
prompt_template_2 = ChatPromptTemplate.from_template("Is this {capital} safe?")

# Create a composed chain that uses the output of the first chain as input to the second prompt
composed_chain = {"capital": chain} | prompt_template_2 | model | output_parser

# Invoke the composed chain with the input country "India" to get the safety information
output_2 = composed_chain.invoke({"country": "India"})

# Print the final output
print(output_2)