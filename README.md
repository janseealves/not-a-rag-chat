# README

## Not a RAG Chat (yet)

Este projeto é um exemplo de chat interativo utilizando Streamlit e LangChain.

### Pré-requisitos

- Python 3.10+
- Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### Como rodar o chat

1. Certifique-se de configurar suas variáveis de ambiente (ex: chave da OpenAI) em um arquivo `.env`.
2. Execute o script pelo Streamlit:

```bash
streamlit run scripts/chat-completion.py
```

3. Acesse o endereço exibido no terminal para interagir com o chat.

### Observações

- Escolha o modelo desejado na interface.
- O histórico da conversa é mantido durante a sessão.
- Consulte a documentação das bibliotecas