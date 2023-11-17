# nlq-app

The goal is to build a natural language question and answer app using LLM on our own data

## Design

|Component | Framework | Function |
|----------|-----------|----------|
| FrontEnd UI | Streamlit | UI |
| LLM Framework | LangChain | composing apps using Language Models, prompt templates, agents or chains |
| LLM | OpenAI | Language Model used |
| Data | NA |  Public Credit Card Complaints dataset on Kaggle |
| Data Store | SQLite (DB) or Apache Spark DataFrame or  Apache Spark SQL|

## Notebooks

* [LangChain_LLM_Database](notebook/LLMs%20with%20SQL.ipynb)
* [LangChain_LLM_SparkDataFrame](notebook/LangChain_LLM_SparkDataFrame.ipynb)
* [LangChain_LLM_SparkSQL](notebook/LangChain_LLM_SparkSQL.ipynb)




