import streamlit as st
import openai

client = openai.OpenAI(
    api_key=st.secrets["api_key"],
    base_url=st.secrets["base_url"]
)


st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://ontracai.com/wp-content/uploads/2024/03/ONTRAC-Logo-Light.png");
            background-size: 30% 10%;
            background-position: 50% 10%;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


st.title(' ')

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

prompt = st.chat_input("Pass your prompt here")

if prompt:
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role':'user', 'content':prompt})

    response = client.responses.create(
    model="llama-3.3-70b-versatile",
    input=prompt
    )
    
    airesponse = response.output_text
    st.chat_message('assistant').markdown(airesponse)

    st.session_state.messages.append({"role": "assistant", "content": airesponse})

