import streamlit as st
import requests

st.set_page_config(
    page_title="SAP Ticket Summarizer",
    page_icon="🤖"
)

st.title("🤖 SAP Ticket Summarizer")

ticket = st.text_area(
    "Enter SAP Ticket Issue"
)

if st.button("Summarize Ticket"):

    if ticket:

        response = requests.post(
            "http://127.0.0.1:8000/summarize",
            json={
                "ticket": ticket
            }
        )

        if response.status_code == 200:

            result = response.json()

            st.subheader("Summary")

            st.json(result)

        else:
            st.error("Backend Error")