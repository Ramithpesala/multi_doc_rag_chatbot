import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="RAG Chat Assistant",
    page_icon="🤖",
     layout="centered"
)

st.title("🗐 Document Chat Assistant")


# Session Memory
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat Input
if prompt := st.chat_input("Ask your documents..."):

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)


    # Build Conversation Context (only last 5 messages will be sent to FastAPI)
    conversation = "\n".join(
        [f"{m['role']}: {m['content']}" for m in st.session_state.messages[-5:]]
    )


    # Send to FastAPI
    try:
        with st.spinner("Thinking..."):

            response = requests.post(
                API_URL,
                json={"question": conversation},
                timeout=60
            )

            response.raise_for_status()

            answer = response.json()["answer"]

    except requests.exceptions.Timeout:
        answer = "⚠️ Server timeout. Try again."

    except requests.exceptions.ConnectionError:
        answer = "⚠️ Cannot connect to FastAPI. Is the server running?"

    except Exception as e:
        answer = f"⚠️ Error: {str(e)}"


    # Save assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })


    with st.chat_message("assistant"):
        st.write(answer)
