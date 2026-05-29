
from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from src.rag.vector_store import get_embeddings


# Project Paths
BASE_DIR = Path(__file__).resolve().parent.parent

KNOWLEDGE_BASE = BASE_DIR / "knowledge_base"
VECTOR_DB = BASE_DIR.parent / "vector_store"


def load_documents():
    """
    Load all markdown files from knowledge base
    """

    documents = []

    for file in KNOWLEDGE_BASE.glob("*.md"):

        content = file.read_text(
            encoding="utf-8"
        )

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "source": file.name
                }
            )
        )

    return documents


def build_vector_store():

    print("Loading documents...")

    documents = load_documents()

    print(f"Documents Loaded: {len(documents)}")

    if len(documents) == 0:
        raise ValueError(
            f"No documents found in {KNOWLEDGE_BASE}"
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(
        documents
    )

    print(f"Chunks Created: {len(chunks)}")

    if len(chunks) == 0:
        raise ValueError(
            "No chunks created from documents."
        )

    print("\nFirst Chunk Preview:\n")

    print(
        chunks[0].page_content[:300]
    )

    embeddings = get_embeddings()

    print("\nEmbedding Model Loaded:")
    print(type(embeddings))

    print("\nTesting Embedding Generation...")

    test_embedding = embeddings.embed_query(
        "test attack"
    )

    print(
        f"Embedding Dimension: {len(test_embedding)}"
    )

    print("\nGenerating FAISS Index...")

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    VECTOR_DB.mkdir(
        exist_ok=True
    )

    db.save_local(
        str(VECTOR_DB)
    )

    print(
        f"\nVector Store Saved Successfully: {VECTOR_DB}"
    )

if __name__ == "__main__":

    build_vector_store()