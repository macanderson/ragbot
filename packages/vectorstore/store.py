# packages/vectorstore/store.py
# github.com/macanderson/ragbot
#
# Create and return a Qdrant vectorstore from documents.
#
# Called automatically by `poetry run python scripts/ingest.py`
#
from typing import Optional
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def get_vectorstore(
    file_path: str = "data/corpus.txt",
    chunk_size: int = 500,
    chunk_overlap: int = 50,
    collection_name: str = "rag_chatbot",
    embedding_model: Optional[OpenAIEmbeddings] = None
) -> Qdrant:
    """
    Create and return a Qdrant vectorstore from documents.

    Args:
        file_path: Path to the text file to load
        chunk_size: Size of text chunks for splitting
        chunk_overlap: Overlap between chunks
        collection_name: Name of the Qdrant collection
        embedding_model: Optional custom embedding model

    Returns:
        Qdrant vectorstore instance
    """
    # Load and split documents
    docs: list[Document] = TextLoader(file_path).load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    split_docs = splitter.split_documents(docs)

    # Initialize embedding model if not provided
    if embedding_model is None:
        embedding_model = OpenAIEmbeddings()

    # Create and return vectorstore
    return Qdrant.from_documents(
        documents=split_docs,
        embedding=embedding_model,
        collection_name=collection_name
    )
