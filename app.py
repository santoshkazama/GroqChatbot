import streamlit as st
import openai

client = openai.OpenAI(
    api_key=st.secrets["api_key"],
    base_url=st.secrets["base_url"]
)


st.markdown(
        """
        <style>
        .fixed-header {
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
          height: 180px;
          background: url("https://ontracai.com/wp-content/uploads/2024/03/ONTRAC-Logo-Light.png");
          background-size: 30% 10%;
          background-position: center center;
          background-repeat: no-repeat;
          background-color: #0E1117;
          z-index: 999;
          display: flex;
          align-items: center;
          justify-content: center;
          background-size: 30% 36%;
    } 
    .fixed-header::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 35%;
        width: 30%;
        height: 2px;
        background: #1E88E5;
        border-radius: 1px;
    }
        </style>
        """,
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="fixed-header"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

st.markdown('</div>', unsafe_allow_html=True)

prompt = st.chat_input("Pass your prompt here")

if prompt:
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role':'user', 'content':prompt})

    response = client.responses.create(
    model="llama-3.1-8b-instant",
    input=prompt
    )
    
    airesponse = response.output_text
    st.chat_message('assistant').markdown(airesponse)
    st.session_state.messages.append({"role": "assistant", "content": airesponse})



