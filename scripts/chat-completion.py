from dotenv import load_dotenv
from langchain.chat_models import init_chat_model #Buscar na documentação do LangChain

import streamlit as st
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO, format="{levelname}:{name}:{message}", style='{')
logger = logging.getLogger("chat-completion")

async def iterator2generator(async_iter):
    async for chunk in async_iter:
        yield chunk.content # Pausa, retorna o chunk.content e continua para o próximo chunk

st.set_page_config(page_icon='💬')
st.title("Not a RAG Chat")

if model:= st.selectbox('Select a model:', ('GPT-4 Turbo', 'GPT-4.1 mini', 'GPT-4.1 nano')):
    try:
        chat = init_chat_model(f'openai:{model.lower().replace(' ', '-')}')

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
                    response_stream = chat.astream(prompt) # O método .asstream() retorna um objeto do tipo AsyncIterator
                    response = st.write_stream(iterator2generator(response_stream)) # .write_stream() espera um objeto do tipo AsyncGenerator ou uma função que yielde valores
                    st.session_state.messages.append({'role': 'assistant', 'content': response})
                except Exception as e:
                    logger.error(f'Erro na resposta da LLM: {e}')

    except Exception as e: 
        logger.error(f'Erro ao inicializar o modelo: {e}')
