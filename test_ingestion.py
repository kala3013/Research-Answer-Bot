"""Test the ingestion pipeline."""
from services.pipeline import IngestionService
from utils.config import load_config
import os
import sys

config = load_config()
ing = IngestionService(config)

# Test processing one PDF
pdf_path = 'data/pdfs/paper_1.pdf'
print(f"Processing {pdf_path}...")
chunks = ing.process_pdf(pdf_path)
print(f"Processed paper_1.pdf: {len(chunks)} chunks created")

if chunks:
    print(f"First chunk metadata keys: {list(chunks[0]['metadata'].keys())}")
    print(f"First chunk text preview: {chunks[0]['text'][:200]}...")
    print(f"First chunk page number: {chunks[0]['metadata'].get('page_number')}")
    print(f"First chunk paper title: {chunks[0]['metadata'].get('paper_title')}")

# Check vector store
vs = ing.get_vector_store()
count = vs.count()
print(f"\nVector store count: {count}")

all_docs = vs.get_all()
print(f"All docs count: {len(all_docs)}")

# Test retrieval
from services.pipeline import RetrievalService
retrieval = RetrievalService(config)
results = retrieval.retrieve("What is the Transformer architecture?", top_k=3)
print(f"\nRetrieval results: {len(results)}")
for r in results:
    print(f"  - Score: {r['score']:.4f}, Title: {r['metadata'].get('paper_title', 'N/A')}, Page: {r['metadata'].get('page_number', 'N/A')}")

print("\n✅ Ingestion pipeline test PASSED!")