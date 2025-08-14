from dotenv import load_dotenv
from langchain.chat_models import init_chat_model #Buscar na documentação do LangChain

import streamlit as st
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO, format='{levelname}:{name}:{message}', style='{')
logger = logging.getLogger('chat-completion')

st.set_page_config(page_icon='💬')
st.title('Not a RAG Chat')

with st.expander('Setup ⚙️'):
    model = st.selectbox('Model:', ('GPT-4 Turbo', 'GPT-4.1 mini', 'GPT-4.1 nano'))
    temperature = st.slider('Temperature:', 0.0, 1.0, 0.3, 0.1)
    memory_size = st.slider('Memory Size:', 0, 20, 10, 1)

if model:
    try:
        chat = init_chat_model(f'openai:{model.lower().replace(' ', '-')}', temperature=temperature)

        # Responsável por preservar o histórico da conversa mesmo com a 're-renderização' da página
        if 'messages' not in st.session_state:
            st.session_state.messages = []  
        for message in st.session_state.messages:
            with st.chat_message(message['role']):
                st.markdown(message['content'])

        # Lógica do Chat 
        if prompt:= st.chat_input('What is up?'): 
            with st.chat_message('user'):
                st.markdown(prompt)
                st.session_state.messages.append({'role': 'user', 'content': prompt})

            with st.chat_message('ai'):
                try:
                    response_stream = chat.stream(st.session_state.messages)
                    response = st.write_stream(response_stream)
                    st.session_state.messages.append({'role': 'assistant', 'content': response})
                    logger.info(response)
                except Exception as e:
                    logger.error(f'Erro na resposta da LLM: {e}')

        # Clear messages history
        if len(st.session_state.messages) >= memory_size:
            import time
            
            with st.status('Memory limit exceeded, resetting cache...') as status:
                st.session_state.messages.clear()
                time.sleep(2)
                status.update(label= 'Memory lost!', state='complete')

    except Exception as e: 
        logger.error(f'Erro ao inicializar o modelo: {e}')
