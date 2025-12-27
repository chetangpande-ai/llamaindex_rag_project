# 📚 LlamaIndex – Naive RAG Implementation

## Overview

**LlamaIndex** is a data framework designed to connect **Large Language Models (LLMs)** with **external and private data sources**.  
In this project, LlamaIndex is used to build a **Naive Retrieval-Augmented Generation (RAG)** pipeline that allows an LLM to answer questions based on custom documents.

This repository demonstrates a **simple, minimal RAG setup** focusing on:
- Document ingestion
- Vector indexing
- Semantic retrieval
- LLM-based response generation

---

## What is Naive RAG?

**Naive RAG** is the simplest form of Retrieval-Augmented Generation:

User Query
↓
Vector Search (Top-K Chunks)
↓
LLM Prompt + Retrieved Context
↓
Final Answer


There is **no reranking**, **no query rewriting**, and **no multi-step reasoning**.

This makes it ideal for:
- Learning RAG fundamentals
- Proof-of-concept projects
- Internal knowledge bots

---

## Why LlamaIndex?

LlamaIndex focuses specifically on the **data layer** of GenAI applications.

It handles:
- Document loading (PDFs, TXT, DBs, APIs)
- Chunking and node management
- Vector indexing
- Retrieval logic
- Context injection into LLM prompts

You focus on **what data to use**, not **how to wire everything manually**.

---

## High-Level Architecture

Documents (TXT / PDF)
↓
LlamaIndex
(Chunk + Embed)
↓
Vector Index
↓
Semantic Retriever
↓
LLM (Groq / OpenAI / Local)
↓
Answer


---

## Key Components Used

| Component | Purpose |
|--------|--------|
| `SimpleDirectoryReader` | Loads documents from disk |
| `VectorStoreIndex` | Creates vector embeddings and index |
| HuggingFace Embeddings | Local, free vector embeddings |
| LLM (Groq / Local) | Generates final answer |

---

## Why This is Called “Naive”

This implementation intentionally avoids:
- Query expansion
- Rerankers
- Feedback loops
- Agent-based reasoning

It uses:
- Single vector search
- Direct LLM response

This keeps the system:
- Easy to debug
- Easy to explain
- Easy to test

---

## LlamaIndex vs LangChain

| Feature | LlamaIndex | LangChain |
|------|-----------|-----------|
| Primary Focus | Data + Retrieval | Orchestration + Agents |
| RAG Setup | Very simple | More manual |
| Learning Curve | Low | Medium–High |
| Indexing | Built-in | External |
| Agents / Tools | Limited | Strong |
| Best For | RAG, document QA | Complex workflows |

### When to choose **LlamaIndex**
- Document-centric RAG
- Internal knowledge bots
- Fast prototyping
- Minimal configuration

### When to choose **LangChain**
- Multi-tool agents
- Complex workflows
- Tool calling
- Autonomous reasoning chains

👉 **Common Industry Pattern**  
Use **LlamaIndex for retrieval** + **LangChain for orchestration**

---

## LlamaIndex vs Other Options

### LlamaIndex vs Raw Vector DB (FAISS / Pinecone)

| Aspect | LlamaIndex | Vector DB Only |
|-----|-----------|---------------|
| Chunking | Built-in | Manual |
| Retrieval Logic | Built-in | Manual |
| Prompt Injection | Built-in | Manual |
| Learning Speed | Fast | Slower |
| Control | Medium | High |

---

## Pros of LlamaIndex

✅ Excellent for RAG use cases  
✅ Minimal boilerplate  
✅ LLM-agnostic (Groq, OpenAI, Local)  
✅ Built-in document loaders  
✅ Strong community support  

---

## Cons of LlamaIndex

❌ Limited agent support  
❌ Less flexible than LangChain for workflows  
❌ Abstractions may hide low-level control  
❌ Not ideal for complex multi-step reasoning  

---

## Ideal Use Cases

- Company knowledge base
- Policy / documentation chatbot
- Test case or requirement search (QA)
- Internal AI assistants
- Learning and PoC projects

---

## When NOT to Use LlamaIndex

- Heavy agent-based systems
- Complex tool orchestration
- Long-running autonomous workflows
- Fine-grained control over every LLM call

---

## Interview-Ready Summary

> “LlamaIndex is a data framework optimized for Retrieval-Augmented Generation. It simplifies document ingestion, indexing, and retrieval, making it ideal for building knowledge-centric AI applications.”

---

## Next Steps

- Add PDF support
- Persist vector index
- Add reranking
- Introduce evaluation metrics
- Combine with LangChain agents

---

## License

MIT
