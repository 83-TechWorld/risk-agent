from langchain_openai import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import PromptTemplate
from db import db
from config import settings
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from config import settings  # Assuming y

llm = ChatOpenAI(
    model="gpt-3.5-turbo",        # Or "gpt-4" if you have access
    openai_api_key=settings.openai_api_key,
    temperature=0,                # Optional: how random you want (0 = most stable)
    max_tokens=1000               # Optional: max tokens in response
)


prompt = PromptTemplate(
    input_variables=["input", "table_info", "top_k"],
    template="""
You are a risk management AI agent. You are given the table kri_indicators(ref TEXT, value INTEGER, status TEXT).
Use safe SQL. Here are examples:

- Insert: "Insert a KRI called 'Cyber Attack' with value 90 and status 'High'."
- Update: "Update value of 'Vendor Risk' to 70."
- Delete: "Delete KRI with ref 'Old Risk Control'."

Question:
{input}

SQL Query:
"""
)

db_chain = SQLDatabaseChain.from_llm(
    llm,
    db
)
