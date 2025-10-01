import os
import configparser
from langchain_deepseek import ChatDeepSeek
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain.prompts import ChatPromptTemplate

# constantes
PATH_DB = 'db/collection/my_pdfs/storage.sqlite'
PARSER = configparser.ConfigParser()
PARSER.read("env.conf")
OPENAI_API_KEY = PARSER.get('credentials','OPENAI_API_KEY')
EMBEDDING = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=OPENAI_API_KEY)
DEEPSEEK_API_KEY = PARSER.get("credentials","DEEPSEEK_API_KEY")
os.environ["DEEPSEEK_API_KEY"] = DEEPSEEK_API_KEY

# prompt inicial
prompt_template = """
Você é uma IA que consulta um banco de dados vetorial.
As informações que você dirá, vieram de documentos PDF de dicionários de dados do Portal de Dados Abertos do ONS.
Responda a pergunta "{pergunta}" como um analista de dados sênior
com base nas informacoes da tabela:
{base_conhecimento}
Se voce nao tiver certeza sobre a resposta, retorne: Desculpe, não sei como te ajudar no momento.
Lembre-se que os dicionários de dados geralmente colocam na coluna <descrição> as colunas do dataset.
"""

# carregando banco de dados vetorial
db = QdrantVectorStore.from_existing_collection(
    collection_name="metadata_ons",
    embedding=EMBEDDING,
    path= './db'
)

def question():
    pergunta = input("Pergunte no ChatONS >> ")

    # comparar a pergunta do usuario (embedding) com o banco de dados
    res = db.similarity_search_with_relevance_scores(pergunta, k=3)

    text_responses = []

    for response in res:
        texto = response[0].page_content 
        text_responses.append(texto)

    base_conhecimento = "\n\n----\n\n".join(text_responses)
    
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )

    prompt_template_obj = ChatPromptTemplate.from_template(prompt_template)
    prompt_messages = prompt_template_obj.invoke({
        "pergunta": pergunta, 
        "base_conhecimento": base_conhecimento
    })
    
    resposta = llm.invoke(prompt_messages)
    print("Resposta da AI: ", resposta.content)

question()