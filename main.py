from dotenv import load_dotenv
load_dotenv()

from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    Settings
)

from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def main():
    # 1. Configure Groq LLM
    Settings.llm = Groq(
        model="llama-3.1-8b-instant",
        temperature=0.2
    )

    # 2. Configure embeddings (local, free)
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 3. Load documents
    documents = SimpleDirectoryReader("data").load_data()

    # 4. Create vector index
    index = VectorStoreIndex.from_documents(documents)

    # 5. Query engine
    query_engine = index.as_query_engine()

    response = query_engine.query(
        "What is LlamaIndex used for?"
    )

    print("\nAnswer:")
    print(response)

if __name__ == "__main__":
    main()
