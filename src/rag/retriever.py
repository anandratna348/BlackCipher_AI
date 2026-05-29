# src/rag/retriever.py

from pathlib import Path

from langchain_community.vectorstores import FAISS

from src.rag.vector_store import get_embeddings


BASE_DIR = Path(__file__).resolve().parent.parent
VECTOR_DB = str(BASE_DIR.parent / "vector_store")


def get_retriever():

    db = FAISS.load_local(
        VECTOR_DB,
        get_embeddings(),
        allow_dangerous_deserialization=True
    )

    return db.as_retriever(
        search_kwargs={"k": 3}
    )


def retrieve_context(query: str):

    retriever = get_retriever()

    docs = retriever.invoke(query)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context