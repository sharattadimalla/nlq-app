"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st

st.title("Sherlock Holmes Investigative NLQ Service 🎈")
st.sidebar.markdown("# Main 🎈)


def get_entity(user_prompt: str) -> str:
    """get_entities uses NLP to identify Entities

    Args:
        user_prompt (str): user provided prompt

    Returns:
        str: Identifies entity
    """
    return "Micrsoft"


def lookup_entity_summary(entity_nm: str) -> dict:
    """Returns high level summary of entity

    Args:
        entity (str): name of entity

    Returns:
        dict: _description_
    """
    return {}


# create a method to lookup entity - Detail Info
def lookup_entity_details(entity_id: str) -> dict:
    """Returns detail level information of entity

    Args:
        entity_id (str): Unique identifier of an entity

    Returns:
        dict: _description_
    """
    return {}


prompt = st.chat_input(placeholder="Ask me a question", max_chars=1000)
if prompt:
    st.write(f"Did you ask for : {get_entity(prompt)}")
