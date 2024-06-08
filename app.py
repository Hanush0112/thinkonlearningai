import streamlit as st
import time
from PIL import Image
from langchain_community.llms import Ollama


st.set_page_config(page_title='Thinkon Learning AI',
                   page_icon='thinkon learning app.jpg',
                   layout='wide',
                   initial_sidebar_state='expanded'
                )


SYSTEM_PROMPT = """your name is thinkon assistant
You are a helpful and respectful and honest AI assistant. Always answer as helpfully as possible.
If you don't know the answer to a question, don't share false information. Your school teacher. you have to make the answers crystal clear. and for single answers only give the answer.
you have to only give the exact answer do not give any expalnation until asked for. Always give short answers. 
"""

def firePrompt(prompt: str, temp=0.2) -> str:
    llm = Ollama(model="mistral",
             system=SYSTEM_PROMPT,
             temperature=temp
             )
    res = llm.invoke(prompt)
    return res


if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'temp' not in st.session_state:
    st.session_state.temp = 0


def getAvatar(role):
    if role == 'assistant':
        return "thinkon learning app.jpg"
    else :
        return "account.png"

def getContext():
    res = ""
    for item in st.session_state.messages[:-1]:
        res = res + f"role : {item['role']} content : {item['content']}\n"
    return res


# Load the image
image = Image.open('thinkon learning app.jpg')

# Display the logo and title side by side
col1, col2 = st.columns([1, 25])
with col1:
    st.image(image, width=50)
with col2:
    st.markdown(
        """
        <div style="display: flex; align-items: center;">
            <h1 style="margin: 0;">Your AI Assistant</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

# Add CSS to lower the image
st.markdown(
    """
    <style>
    [data-testid="stImage"] img {
        margin-top: 20px;  /* Adjust the value as needed to lower the image */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('#### :gray[Powered by Thinkon learning ] ', unsafe_allow_html=True)
st.divider()

with st.chat_message(name="assistant", avatar='thinkon learning app.jpg'):
    st.markdown('Ask me anything! ')
for message in st.session_state.messages:
    with st.chat_message(name=message["role"], avatar=getAvatar(message["role"])):
        st.markdown(f'{message["content"]}')

if prompt := st.chat_input(placeholder="Chat with me!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message(name="user", avatar='account.png'):
        st.markdown(prompt)
    with st.chat_message(name='assistant', avatar='thinkon learning app.jpg'):
        message_placeholder = st.empty()
        full_response = ""
        with st.spinner(text="Hold on a sec"):
            raw = firePrompt(st.session_state.messages[-1]['content'], temp=st.session_state.temp)
            response = str(raw)
        # Simulate stream of response with milliseconds delay
        for chunk in response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(f'<span style="font-size:24px;color:blue"><b>{full_response}</span> <spanstyle="color:blue">▌</span>', unsafe_allow_html=True)
    message_placeholder.markdown(f'<span style="font-size:24px;color:blue"><b>{full_response}</span>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
hide_st_style = """
            <style>
            #MainMenu {visibility:hidden ;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

