import streamlit as st
from google import genai

st.set_page_config(
    page_title="Shivani AI Career Assistant",
    page_icon="🤖"
)

st.title("🤖 Shivani AI Career Assistant")
st.write(
    "Ask me about Shivani's skills, projects, experience and career."
)

# Load knowledge base
with open("knowledge.txt", "r", encoding="utf-8") as file:
    knowledge = file.read()

# Gemini client
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

system_prompt = f"""
You are Shivani Lokhande's AI Career Assistant.

Your job is to answer questions about Shivani's:
- skills
- education
- projects
- work experience
- career direction

Use the knowledge base below as your primary source.

Do not invent information.

If the requested information is not present in the knowledge base,
say that the information is not available.

Keep answers professional, clear and concise.

KNOWLEDGE BASE:
{knowledge}
"""

question = st.chat_input(
    "Ask something about Shivani..."
)

if question:

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=[
                system_prompt,
                f"User question: {question}"
            ]
        )

        st.write(response.text)