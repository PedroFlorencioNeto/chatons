import configparser
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader

# variaveis globais
PATH = "base"
PARSER = configparser.ConfigParser()
PARSER.read("env.conf")
OPENAI_API_KEY = PARSER.get('credentials','OPENAI_API_KEY')
EMBEDDINGS = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=OPENAI_API_KEY)

def create_database():
    documents = load_documents()
    chunks = split_chunks(documents)
    vectorize_chunks(chunks)

def load_documents():
    loader  = PyPDFDirectoryLoader(PATH, glob="*.pdf")
    docs = loader.load()
    return docs

def split_chunks(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 100,
        length_function = len,
        add_start_index=True
    )
    chunks = splitter.split_documents(docs)
    return chunks

def vectorize_chunks(chunks):
    QdrantVectorStore.from_documents(
        chunks,
        embedding=EMBEDDINGS,
        path="./db",
        collection_name="metadata_ons"
    )
    
create_database()