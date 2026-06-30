from pathlib import Path

from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents(kb_dir: Path) -> list[Document]:
    """Legge ogni .md in kb_dir e ne fa un Document con metadata['source']."""
    docs: list[Document] = []
    files = kb_dir.glob("*.md")
    for file in files:
        testo = file.read_text(encoding="utf-8")
        docs.append(Document(page_content=testo, metadata={"source": file.name}))

    return docs


def split_documents(docs: list[Document]) -> list[Document]:
    """Spezza i Document in chunk, preservando i metadati (source)."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=80)
    return splitter.split_documents(docs)


def build_store(chunks: list[Document]) -> InMemoryVectorStore:
    """Crea embedding locali (fastembed) e li mette in un vector store in memoria."""
    return InMemoryVectorStore.from_documents(chunks, embedding=FastEmbedEmbeddings())
