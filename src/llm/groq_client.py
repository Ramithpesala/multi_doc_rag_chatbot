from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()


def get_llm():
    load_dotenv()
    groq_api_key = os.getenv("GROQ_API_KEY")

    return ChatGroq(
        api_key=groq_api_key,
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        max_tokens=1024
    )