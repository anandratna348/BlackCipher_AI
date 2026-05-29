from src.rag.retriever import retrieve_context

context = retrieve_context(
    "Exploit attack"
)

print(context)