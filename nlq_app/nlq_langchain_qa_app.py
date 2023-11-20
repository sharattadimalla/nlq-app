"""
# LLM Application
"""
import os
from pathlib import Path
import dotenv
import streamlit as st
from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI

# from langchain_experimental.sql import SQLDatabaseChain
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_types import AgentType
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit

from pygpt4all.models.gpt4all import GPT4All

from load_file import Data

# load dotenv to setup OPENAI_API_KEY
dotenv.load_dotenv()

# Title for Home Page
st.title(
    """
    :sparkles: Sherlock Investigative Service: Natural language style Q&A
    Powered by Streamlit,LangChain,LLM & data
    """
)

# Sidebar
LLMs = ["OpenAI", "GPT4All"]
DATASETS = ["CFPB_Complaints"]
with st.sidebar:
    selected_llm = st.sidebar.radio("Select an LLM", list(LLMs))
    selected_data = st.sidebar.radio("Select a Dataset", list(DATASETS))

# Setup db, table and data
FILE_NM = "credit_card_complaints.csv"
FILE_PATH = "/Users/sharattadimalla/github/nlq-app/public_data/"
TABLE_NM = "customer_complaints"
data = Data(file_name=FILE_NM, file_path=FILE_PATH)
data.create_table(TABLE_NM)
db = SQLDatabase.from_uri("sqlite:///customer_complaints_db.sqlite")

# llm
if selected_llm == "OpenAI":
    llm = OpenAI(temperature=0)
elif selected_llm == "GPT4All":
    llm = OpenAI(temperature=0)

# create agent
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    agent_executor_kwargs={"return_intermediate_steps": True},
)


def generate_response(user_input: str) -> object:
    """Return LLM response for the user question

    Args:
        user_input (str): user question

    Returns:
        str: LLM response
    """

    resp = agent_executor.__call__(user_input)
    with st.expander("See Agent Thinking"):
        st.write(resp["intermediate_steps"])
    st.write(resp["output"])


with st.form("my_form"):
    text = st.text_input(
        "Ask me a question:", "Ex:- How many total complaints are there?"
    )
    submitted = st.form_submit_button("submit")
    if submitted:
        generate_response(text)
