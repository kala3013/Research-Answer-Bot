# Research Paper Answer Bot

## Project Overview
The Research Paper Answer Bot is a Retrieval-Augmented Generation (RAG) system designed to provide answers to user queries based on a curated collection of research papers in the fields of Generative AI, Large Language Models, and Machine Learning. The system allows users to upload research paper PDFs, extract text, and generate grounded answers using advanced language models.

## Problem Statement
As the volume of research papers increases, it becomes challenging for researchers and practitioners to quickly find relevant information. This project aims to streamline the process of retrieving and understanding research content through an intelligent answer bot.

## Objectives
- Develop a system that can ingest, process, and retrieve information from research papers.
- Implement various embedding and retrieval strategies to enhance answer accuracy.
- Provide a user-friendly interface for interaction with the system.

## Features
- Upload and process research paper PDFs.
- Extract text and metadata from PDFs, including handling scanned documents with OCR.
- Generate embeddings and store them in a vector database.
- Retrieve relevant document chunks and provide grounded answers using an LLM.
- Support multi-turn conversational queries.
- Evaluate retrieval and answer quality with metrics.

## Architecture
The system is built using a microservices architecture, with separate components for ingestion, embeddings, retrieval, and the RAG pipeline. FastAPI serves as the backend, while Streamlit provides the frontend interface.

## RAG Workflow
1. User uploads a research paper.
2. The system extracts text and metadata.
3. Embeddings are generated and stored in a vector database.
4. User queries are processed and relevant chunks are retrieved.
5. The LLM generates answers based on the retrieved context.
6. The system displays the top supporting sources for each answer.

## Dataset
The dataset consists of at least 10 research papers related to Generative AI, Large Language Models, and other relevant topics. The papers are stored in the `data/pdfs` directory.

## Installation
To set up the project, follow these steps:
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up environment variables as specified in the `.env.example` file.

## Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key for accessing the language model.

## Running Locally
To run the application locally, execute the following commands:
1. Start the FastAPI backend: `uvicorn backend.main:app --reload`
2. Launch the Streamlit frontend: `streamlit run app.py`

## Running with Docker
To run the application using Docker, use the following command:
```bash
docker-compose up
```

## Dataset Download
To download the dataset, run the following script:
```bash
python scripts/download_dataset.py
```

## Document Indexing
To index the documents, execute:
```bash
python scripts/ingest.py
```

## Embedding Experiments
To run embedding experiments, use:
```bash
python scripts/run_embedding_experiment.py
```

## Retrieval Experiments
To execute retrieval experiments, run:
```bash
python scripts/run_retrieval_experiment.py
```

## Evaluation
To evaluate the RAG system, execute:
```bash
python scripts/evaluate.py
```

## Streamlit Usage
Access the Streamlit application in your web browser to interact with the Research Paper Answer Bot.

## FastAPI Usage
The FastAPI application provides endpoints for document management, querying, and evaluation.

## Testing
Run tests using pytest to ensure all functionalities work as expected:
```bash
pytest
```

## Troubleshooting
If you encounter issues, check the logs for errors and ensure all dependencies are correctly installed.

## Future Improvements
- Expand the dataset with more research papers.
- Enhance the UI/UX of the Streamlit application.
- Implement additional retrieval strategies for improved performance.