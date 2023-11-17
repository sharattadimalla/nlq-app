# nlq-app

The goal is to build a natural language question and answer app using LLM on our own data

## Design

FrontEnd Framework --> Streamlit (Serves as UI)
LLM Framework --> LangChain (composable application using Language Models, prompt templates, agents or chains)
LLM --> OpenAI (Language Model used)
Data --> Public Credit Card Complaints dataset on Kaggle
Data Store SQLite (DB) | Apache Spark DataFrame | Apache Spark SQL

## Notebooks

* [LangChain_LLM_Database](notebook/LLMs%20with%20SQL.ipynb)
* [LangChain_LLM_SparkDataFrame](notebook/LangChain_LLM_SparkDataFrame.ipynb)
* [LangChain_LLM_SparkSQL](notebook/LangChain_LLM_SparkSQL.ipynb)




