from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_vectorstore():
    docs = TextLoader("data/corpus.txt").load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)
    vectorstore = Qdrant.from_documents(
        documents=split_docs,
        embedding=OpenAIEmbeddings(),
        collection_name="rag_chatbot"
    )
    return vectorstore
