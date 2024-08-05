from langfuse.decorators import langfuse_context, observe
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langfuse import Langfuse

load_dotenv("/Users/vishnumallela/Documents/Learning/LangChain/py.env")

# Initialize LLM (OpenAI)
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
parser = StrOutputParser()


chain = llm | parser

langfuse = Langfuse(
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    host=os.getenv("LANGFUSE_HOST")
)

@observe()  
def main():
    
 
    langfuse_context.update_current_trace(
        metadata={
            "groupId": "1234567890",
            "sessionId": "1234567890",
            "historyId": "9876543210",
            "agentName": "test-agent-2"
        }
    )
    
    # Get the Langchain handler for the current trace
    langfuse_handler = langfuse_context.get_current_langchain_handler()
 

 
    # Add Langfuse handler as callback (classic and LCEL)
    chain.invoke("Who is RajiniKanth", config={"callbacks": [langfuse_handler]})
 
if __name__ == "__main__":
    main()