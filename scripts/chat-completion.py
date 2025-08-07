from dotenv import load_dotenv
from langchain.chat_models import init_chat_model #Buscar na documentação do LangChain
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

chatGPT_nano = init_chat_model("openai:gpt-4.1-nano")

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Translate the following English text to {language}"),
    ("human", "{text}")
])

languages = ["French", "Spanish", "German", "Italian", "Portuguese"]

for language in languages:
    prompt = prompt_template.format_messages(language=language, text="Hello,  World!")

    response = chatGPT_nano.invoke(prompt)

    print(f"{language}: {response.content}") 
