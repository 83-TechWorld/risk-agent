from langchain_openai import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import PromptTemplate
from db import db
from config import settings
from langchain_community.llms import Ollama

llm = Ollama(
    model="phi"   # This tells LangChain to talk to your local Phi model via Ollama server
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
