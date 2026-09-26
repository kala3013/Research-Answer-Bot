"""Test the full RAG pipeline end-to-end."""
from services.pipeline import IngestionService, RetrievalService
from utils.config import load_config
import os

config = load_config()

# Step 1: Index all PDFs
print("=" * 60)
print("STEP 1: Indexing all PDFs")
print("=" * 60)

ingestion = IngestionService(config)
chunks = ingestion.index_all_pdfs()
print(f"Total chunks created: {len(chunks)}")

# Check vector store
vs = ingestion.get_vector_store()
print(f"Vector store count: {vs.count()}")

# Step 2: Test retrieval
print("\n" + "=" * 60)
print("STEP 2: Testing Retrieval")
print("=" * 60)

retrieval = RetrievalService(config)

test_questions = [
    "What is the Transformer architecture?",
    "What is Retrieval-Augmented Generation?",
    "What is the main contribution of the BERT paper?",
]

for q in test_questions:
    print(f"\nQuery: {q}")
    results = retrieval.retrieve(q, top_k=3)
    for r in results:
        meta = r["metadata"]
        title = meta.get("paper_title") or meta.get("title") or meta.get("filename")
        page = meta.get("page_number", 0)
        print(f"  - Score: {r['score']:.4f}, Title: {title}, Page: {page}")

# Step 3: Test answer generation
print("\n" + "=" * 60)
print("STEP 3: Testing Answer Generation")
print("=" * 60)

for q in test_questions:
    print(f"\nQuestion: {q}")
    result = retrieval.answer_question(q)
    print(f"Answer: {result['answer'][:200]}...")
    print(f"Confidence: {result['confidence']:.4f}")
    print(f"Sources: {len(result['sources'])}")
    for s in result['sources']:
        print(f"  - {s['title']} (Page {s['page']}), Score: {s['score']:.4f}")

# Step 4: Test no-answer behavior
print("\n" + "=" * 60)
print("STEP 4: Testing No-Answer Behavior")
print("=" * 60)

result = retrieval.answer_question("What is the meaning of life according to these papers?")
print(f"Question: What is the meaning of life according to these papers?")
print(f"Answer: {result['answer'][:200]}")
print(f"Sources: {len(result['sources'])}")

# Step 5: Test follow-up question
print("\n" + "=" * 60)
print("STEP 5: Testing Follow-up Question")
print("=" * 60)

result1 = retrieval.answer_question("What is the Transformer architecture?")
print(f"Q1: What is the Transformer architecture?")
print(f"A1: {result1['answer'][:100]}...")

result2 = retrieval.answer_question("What are its key components?")
print(f"Q2: What are its key components?")
print(f"A2: {result2['answer'][:100]}...")

print("\n" + "=" * 60)
print("FULL RAG PIPELINE TEST COMPLETE")
print("=" * 60)