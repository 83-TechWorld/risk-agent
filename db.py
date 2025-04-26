from sqlalchemy import create_engine
from langchain.utilities import SQLDatabase
from config import settings
import streamlit as st


TARGET_TABLE = "risk_indicator"  # Your primary table

DATABASE_URL = (
    f"postgresql+psycopg2://{settings.postgres_user}:{settings.postgres_password}"
    f"@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"
)
print(DATABASE_URL)


engine = create_engine(DATABASE_URL)

# LangChain Database Wrapper
include_tables = [TARGET_TABLE]
db = SQLDatabase(engine, include_tables=include_tables)
