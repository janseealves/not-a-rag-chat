## Not a RAG Chat (yet)

Este projeto é um exemplo de chat interativo utilizando Streamlit e LangChain.

### Pré-requisitos

- Python 3.10+
- Conta na OpenAI com chave de API válida

### Configuração

1. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

2. Crie um arquivo `.env` na raiz do projeto com sua chave da OpenAI:
```env
OPENAI_API_KEY=sua_chave_aqui
```

### Como rodar o chat

1. Execute o script pelo Streamlit:
```bash
streamlit run scripts/chat-completion.py
```

2. Acesse o endereço exibido no terminal (geralmente `http://localhost:8501`).

3. Escolha o modelo desejado na interface e comece a conversar!

### Observações

- O histórico da conversa é mantido durante a sessão.
- Certifique-se de que sua chave da OpenAI tem créditos disponíveis.