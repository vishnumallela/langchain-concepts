#!/usr/bin/env python
from typing import List
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes
import os
import uvicorn
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv("/Users/vishnumallela/Documents/Learning/LangChain/py.env")

# Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

# Create model
model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))

# Create parser
parser = StrOutputParser()

# Create chain
chain = prompt_template | model | parser

# App definition
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

# Adding chain route
add_routes(app, chain, path="/chain")

#http://localhost:8000/chain/playground/  to try out the chain

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)