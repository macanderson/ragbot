# github.com/macanderson/ragbot
#
# Ingest documents from the data directory into Qdrant vector store.
#
# Called automatically by `poetry run python scripts/ingest.py`
#
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
import os

def ingest_documents():
    """
    Ingest documents from the data directory into Qdrant vector store.
    Returns the vectorstore instance.

    Called automatically by `poetry run python scripts/ingest.py`
    """
    loader = DirectoryLoader("data/", glob="**/*.txt")
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)

    collection_name = os.getenv("QDRANT_COLLECTION_NAME", "ragbot-collection")
    vectorstore = Qdrant.from_documents(
        documents=split_docs,
        embedding=OpenAIEmbeddings(),
        collection_name=collection_name
    )
    return vectorstore

if __name__ == "__main__":
    ingest_documents()
