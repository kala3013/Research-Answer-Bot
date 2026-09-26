<div align="center">

# 🧠 Research Paper Answer Bot

### 🔬 Intelligent Research Assistant powered by RAG, LLMs & Vector Search

<p>
  <b>Upload Research Papers → Retrieve Knowledge → Generate Grounded Answers</b>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/RAG-AI%20Pipeline-8A2BE2?style=for-the-badge" />
</p>

<p>
  <img src="https://img.shields.io/badge/LLM-OpenAI-412991?style=flat-square&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/Vector%20Database-FAISS%2FChroma-00A67E?style=flat-square" />
  <img src="https://img.shields.io/badge/OCR-Supported-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=flat-square&logo=pytest&logoColor=white" />
</p>

<p>
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-rag-pipeline">RAG Pipeline</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-api">API</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

</div>

---

## ✨ Overview

**Research Paper Answer Bot** is an intelligent **Retrieval-Augmented Generation (RAG)** platform that allows users to upload research papers and interact with them through natural-language conversations.

Instead of relying only on an LLM's pre-trained knowledge, the system retrieves relevant information directly from uploaded research papers and uses that context to generate **grounded, source-aware answers**.

The platform is designed for researchers, students, developers and AI practitioners working with:

* 🤖 Generative AI
* 🧠 Large Language Models
* 📚 Machine Learning
* 🔎 Information Retrieval
* 📄 Research Papers
* 🧩 Natural Language Processing

> **Ask questions about research papers without manually searching through hundreds of pages.**

---

# 🎯 Problem Statement

Modern research produces an enormous amount of technical literature. Finding a specific methodology, result, architecture, dataset or conclusion inside multiple research papers can be time-consuming.

Traditional keyword-based search often fails when users ask questions using natural language.

### The solution

This project combines:

**PDF Processing + Semantic Search + Vector Embeddings + Retrieval + LLM Generation**

to create an intelligent research assistant capable of understanding and answering questions using the uploaded research knowledge base.

---

# 🚀 Key Features

<table>
<tr>
<td width="50%">

### 📄 Intelligent PDF Processing

* Upload research papers
* Extract PDF text
* Extract document metadata
* Handle scanned PDFs
* OCR support
* Automatic document chunking

</td>

<td width="50%">

### 🧠 RAG-powered Answers

* Semantic document retrieval
* Context-aware generation
* Grounded responses
* Source-aware answers
* Reduced hallucination
* Multi-document knowledge retrieval

</td>
</tr>

<tr>
<td>

### 🔍 Advanced Retrieval

* Vector embeddings
* Similarity search
* Top-K retrieval
* Retrieval experiments
* Multiple embedding strategies
* Retrieval evaluation

</td>

<td>

### 💬 Conversational AI

* Multi-turn conversations
* Context-aware questions
* Follow-up questions
* Natural language interaction
* Research-focused responses

</td>
</tr>

<tr>
<td>

### 📊 Evaluation

* Retrieval evaluation
* Answer quality evaluation
* Embedding experiments
* Retrieval experiments
* Automated testing

</td>

<td>

### 🖥️ Modern Interface

* Streamlit frontend
* Interactive research assistant
* Upload interface
* Query interface
* Source visualization
* Developer-friendly FastAPI backend

</td>
</tr>
</table>

---

# 🧩 Technology Stack

<div align="center">

| Layer                  | Technologies            |
| ---------------------- | ----------------------- |
| 🎨 Frontend            | Streamlit               |
| ⚡ Backend              | FastAPI                 |
| 🐍 Language            | Python                  |
| 🧠 LLM                 | OpenAI                  |
| 🔢 Embeddings          | Embedding Models        |
| 🗄️ Vector Search      | FAISS / Chroma          |
| 📄 Document Processing | PDF Parser + OCR        |
| 🧪 Testing             | Pytest                  |
| 🐳 Deployment          | Docker / Docker Compose |
| 🔧 Development         | Git + GitHub            |

</div>

---

# 🏗️ Architecture

```text
                         ┌─────────────────────────┐
                         │        USER             │
                         │                         │
                         │ Upload PDF / Ask Query  │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │   STREAMLIT FRONTEND    │
                         │                         │
                         │ Upload • Chat • Sources │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │      FASTAPI API        │
                         │                         │
                         │ Document / Query / Eval │
                         └────────────┬────────────┘
                                      │
                    ┌─────────────────┴─────────────────┐
                    │                                   │
                    ▼                                   ▼
        ┌──────────────────────┐             ┌──────────────────────┐
        │   DOCUMENT INGESTION │             │    QUERY PROCESSING  │
        │                      │             │                      │
        │ PDF → Text → Chunks  │             │ Query → Embedding    │
        │ OCR → Metadata       │             │ → Semantic Search    │
        └──────────┬───────────┘             └──────────┬───────────┘
                   │                                    │
                   ▼                                    ▼
        ┌──────────────────────┐             ┌──────────────────────┐
        │      EMBEDDINGS      │             │   VECTOR DATABASE    │
        │                      │◄───────────►│                      │
        │ Text → Vectors       │             │ Similarity Search    │
        └──────────────────────┘             └──────────┬───────────┘
                                                        │
                                                        ▼
                                             ┌──────────────────────┐
                                             │    TOP-K CONTEXT     │
                                             │                      │
                                             │ Relevant Chunks      │
                                             └──────────┬───────────┘
                                                        │
                                                        ▼
                                             ┌──────────────────────┐
                                             │        LLM           │
                                             │                      │
                                             │ Context + Question   │
                                             └──────────┬───────────┘
                                                        │
                                                        ▼
                                             ┌──────────────────────┐
                                             │   GROUNDED ANSWER    │
                                             │                      │
                                             │ Answer + Sources     │
                                             └──────────────────────┘
```

---

# 🔄 RAG Pipeline

The core of the application follows a complete Retrieval-Augmented Generation workflow.

### 01 — 📤 Upload

User uploads one or more research papers through the Streamlit interface.

```text
Research Paper.pdf
        ↓
Document Upload
```

### 02 — 📑 Extract

The system extracts text, metadata and document information.

```text
PDF
 ↓
Text Extraction
 ↓
OCR if required
 ↓
Metadata
```

### 03 — ✂️ Chunk

Large documents are divided into smaller meaningful chunks.

```text
Research Paper
      ↓
Text Splitting
      ↓
Chunk 01
Chunk 02
Chunk 03
...
Chunk N
```

### 04 — 🔢 Embed

Each chunk is converted into a numerical vector representation.

```text
Text Chunk
    ↓
Embedding Model
    ↓
Vector Representation
```

### 05 — 🗄️ Store

Embeddings are stored inside a vector database for efficient similarity search.

```text
Embeddings
    ↓
Vector Database
    ↓
Semantic Index
```

### 06 — 🔎 Retrieve

When a user asks a question, the system searches for the most relevant chunks.

```text
User Question
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Top-K Relevant Chunks
```

### 07 — 🤖 Generate

The retrieved context is provided to the language model.

```text
Question
   +
Retrieved Context
   ↓
LLM
   ↓
Grounded Answer
```

### 08 — 📚 Cite Sources

The system presents supporting document information along with the answer.

---

# 💡 Example Interaction

### 👤 User

> What are the major challenges of Retrieval-Augmented Generation?

### 🤖 Research Paper Answer Bot

> Retrieval-Augmented Generation can face challenges related to retrieval quality, document chunking, context selection, computational cost and the possibility of generating inaccurate responses when the retrieved context is incomplete or irrelevant.

### 📚 Supporting Sources

```text
Research Paper: RAG Survey.pdf
Relevant Section: Retrieval Challenges
Similarity: 0.91
```

---

# 📂 Project Structure

```text
research-paper-answer-bot/
│
├── 📁 backend/
│   ├── __init__.py
│   ├── main.py
│   ├── routes/
│   ├── services/
│   └── models/
│
├── 📁 data/
│   └── pdfs/
│       ├── paper_01.pdf
│       ├── paper_02.pdf
│       ├── paper_03.pdf
│       └── ...
│
├── 📁 scripts/
│   ├── download_dataset.py
│   ├── ingest.py
│   ├── run_embedding_experiment.py
│   ├── run_retrieval_experiment.py
│   └── evaluate.py
│
├── 📁 tests/
│   ├── test_ingestion.py
│   ├── test_retrieval.py
│   └── test_api.py
│
├── 📄 app.py
├── 📄 requirements.txt
├── 📄 docker-compose.yml
├── 📄 Dockerfile
├── 📄 .env.example
├── 📄 .gitignore
└── 📄 README.md
```

---

# 📚 Dataset

The project uses a curated collection of research papers covering topics such as:

* Generative AI
* Large Language Models
* Retrieval-Augmented Generation
* Machine Learning
* Natural Language Processing
* AI Agents
* Transformer Architectures

The repository is designed to support **at least 10 research papers** inside:

```text
data/pdfs/
```

Additional papers can be added without changing the core architecture.

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/kala3013/research-paper-answer-bot.git

cd research-paper-answer-bot
```

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Configuration

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

You can use `.env.example` as the configuration template.

> ⚠️ Never commit API keys or secrets to GitHub.

---

# 📥 Dataset Download

Download the research-paper dataset:

```bash
python scripts/download_dataset.py
```

Or manually place PDF files inside:

```text
data/pdfs/
```

---

# 🧠 Document Indexing

After adding the research papers, run:

```bash
python scripts/ingest.py
```

This process performs:

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embedding Generation
 ↓
Vector Database
```

---

# 🧪 Embedding Experiments

Compare different embedding strategies:

```bash
python scripts/run_embedding_experiment.py
```

The experiment pipeline can be used to analyze:

* Embedding quality
* Retrieval relevance
* Semantic similarity
* Search performance

---

# 🔍 Retrieval Experiments

Run retrieval experiments:

```bash
python scripts/run_retrieval_experiment.py
```

Possible evaluation dimensions include:

```text
Top-K Retrieval
Similarity Score
Relevant Chunk Ratio
Recall
Precision
```

---

# 📊 Evaluation

Evaluate the complete RAG system:

```bash
python scripts/evaluate.py
```

The evaluation pipeline is designed to analyze both:

### Retrieval Quality

```text
Precision
Recall
Top-K Accuracy
Similarity
```

### Answer Quality

```text
Relevance
Faithfulness
Context Utilization
Groundedness
```

---

# ▶️ Running the Application

## Start FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

Backend:

```text
http://localhost:8000
```

API documentation:

```text
http://localhost:8000/docs
```

## Start Streamlit Frontend

Open another terminal:

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

# 🐳 Docker Deployment

Build and run the complete application using Docker:

```bash
docker-compose up --build
```

Stop containers:

```bash
docker-compose down
```

This provides a reproducible environment for running the application.

---

# 🔌 API

The FastAPI backend exposes services for document management, querying and evaluation.

### Health Check

```http
GET /health
```

### Upload Document

```http
POST /documents/upload
```

### Query Research Papers

```http
POST /query
```

Example request:

```json
{
  "question": "What are the main challenges of RAG?"
}
```

Example response:

```json
{
  "answer": "RAG systems can face challenges related to retrieval quality, context selection and hallucination.",
  "sources": [
    {
      "document": "rag_survey.pdf",
      "score": 0.91
    }
  ]
}
```

> Endpoint names can be adjusted to match the final implementation.

---

# 💬 Multi-Turn Conversation

The chatbot is designed to maintain conversational context.

### Example

```text
User:
What is RAG?

Bot:
RAG combines information retrieval with language generation...

User:
Why is it useful?

Bot:
It is useful because the model can retrieve external knowledge...

User:
What are its limitations?

Bot:
Based on the retrieved research papers, major limitations include...
```

This allows users to explore complex research topics naturally.

---

# 🧪 Testing

Run the complete test suite:

```bash
pytest
```

For verbose output:

```bash
pytest -v
```

Testing covers components such as:

* Document ingestion
* Text processing
* Retrieval
* API functionality
* Core RAG pipeline

---

# 🔬 Research & Experimentation

One of the main goals of this project is to make the RAG pipeline experimentally measurable.

The architecture allows experimentation with:

```text
┌──────────────────────────────┐
│       RAG Experiments        │
├──────────────────────────────┤
│                              │
│  Chunk Size                  │
│  Chunk Overlap               │
│  Embedding Models            │
│  Retrieval Strategies        │
│  Top-K Values                │
│  Similarity Thresholds       │
│  Prompt Strategies           │
│  LLM Models                  │
│                              │
└──────────────────────────────┘
```

This makes the project suitable not only as an application but also as an **AI/ML experimentation platform**.

---

# 🛡️ Hallucination Reduction Strategy

The system follows a grounding-first approach.

```text
User Question
      ↓
Retrieve Evidence
      ↓
Provide Evidence to LLM
      ↓
Generate Answer
      ↓
Show Supporting Sources
```

The goal is to encourage answers that are based on retrieved research content rather than unsupported model knowledge.

---

# 🎨 Frontend Experience

The Streamlit interface can be designed around a modern research workspace:

```text
┌─────────────────────────────────────────────┐
│ 🧠 Research Paper Answer Bot                │
│ AI-powered research assistant              │
├─────────────────────────────────────────────┤
│                                             │
│ 📄 Upload Papers                            │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Drag & Drop Research Papers             │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ 📚 Knowledge Base                           │
│ 10+ Research Papers                         │
│                                             │
├─────────────────────────────────────────────┤
│                                             │
│ 💬 Ask your research question...            │
│                                             │
│ [ What does this paper propose? ]           │
│                                             │
├─────────────────────────────────────────────┤
│ 🤖 AI Answer                                │
│                                             │
│ Detailed grounded response...               │
│                                             │
├─────────────────────────────────────────────┤
│ 📚 Supporting Sources                       │
│                                             │
│ Paper 01        Similarity: 91%             │
│ Paper 04        Similarity: 87%             │
│                                             │
└─────────────────────────────────────────────┘
```

### Recommended UI Features

* 🌙 Dark / Light mode
* 📄 Drag-and-drop PDF upload
* 💬 Chat-style interface
* 📚 Source cards
* 🔎 Search history
* 📊 Retrieval score visualization
* 🧠 Model information panel
* ⚡ Loading animations
* 📌 Citation/source panel
* 📈 Evaluation dashboard
* 📱 Responsive layout

---

# 🔐 Security Considerations

The project follows basic security practices:

* API keys stored in environment variables
* `.env` excluded from Git
* Input validation
* File type validation
* Backend API separation
* No secrets committed to source control

Recommended `.gitignore` entries:

```gitignore
.env
venv/
__pycache__/
*.pyc
.streamlit/secrets.toml
vector_store/
```

---

# 📈 Future Improvements

### 🤖 AI Improvements

* [ ] Hybrid keyword + semantic retrieval
* [ ] Reranking models
* [ ] Query expansion
* [ ] Multi-query retrieval
* [ ] Adaptive chunking
* [ ] Advanced citation generation
* [ ] Agentic research workflow

### 📊 Evaluation

* [ ] RAGAS integration
* [ ] Faithfulness evaluation
* [ ] Answer relevancy evaluation
* [ ] Context precision
* [ ] Context recall
* [ ] Automated benchmark dashboard

### 🎨 Frontend

* [ ] Advanced research dashboard
* [ ] PDF preview
* [ ] Highlight retrieved passages
* [ ] Conversation history
* [ ] Research paper comparison
* [ ] Citation export
* [ ] Markdown / PDF answer export

### ☁️ Deployment

* [ ] Docker production deployment
* [ ] Cloud deployment
* [ ] CI/CD pipeline
* [ ] Authentication
* [ ] User-specific document collections
* [ ] Scalable vector database

---

# 🌐 Production Architecture

The project can be extended into a production-ready AI research platform:

```text
                    USERS
                      │
                      ▼
              ┌───────────────┐
              │  Web Frontend │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ API Gateway   │
              └───────┬───────┘
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
      Ingestion   Retrieval     Auth
       Service      Service     Service
          │           │
          ▼           ▼
      Document      Vector DB
       Storage         │
                      ▼
                     LLM
                      │
                      ▼
                Grounded Answer
```

---

# 🎓 Learning Outcomes

This project demonstrates practical experience in:

* Retrieval-Augmented Generation
* Large Language Models
* Vector databases
* Semantic search
* Embeddings
* Natural Language Processing
* PDF processing
* OCR
* FastAPI
* Streamlit
* Docker
* API development
* AI evaluation
* Software architecture
* Testing
* Git & GitHub

---

# 💼 Resume Value

### Research Paper Answer Bot — RAG-based AI Research Assistant

> Developed a Retrieval-Augmented Generation system using Python, FastAPI, Streamlit, vector embeddings and LLMs to process research papers, perform semantic retrieval and generate grounded answers with supporting sources. Implemented PDF/OCR ingestion, conversational querying, retrieval experiments and evaluation pipelines with Docker-based deployment support.

---

# 🏆 Why This Project Stands Out

This project combines several modern software engineering and AI concepts into one complete system:

```text
                    RESEARCH PAPER
                           │
                           ▼
                    DOCUMENT AI
                           │
                           ▼
                      EMBEDDINGS
                           │
                           ▼
                     VECTOR SEARCH
                           │
                           ▼
                         RAG
                           │
                           ▼
                         LLM
                           │
                           ▼
                    GROUNDED ANSWER
                           │
                           ▼
                    SOURCE CITATION
```

It demonstrates the complete journey from **raw research documents → machine-readable knowledge → semantic retrieval → AI-generated answers**.

---

# 👨‍💻 Author

<div align="center">

### Kalanidhi M C

**Computer Science Engineering Student | Full Stack Developer | AI/ML Enthusiast**

📍 Tamil Nadu, India

<a href="https://github.com/kala3013">
<img src="https://img.shields.io/badge/GitHub-kala3013-181717?style=for-the-badge&logo=github" />
</a>

<a href="mailto:kalanidhimurugan@gmail.com">
<img src="https://img.shields.io/badge/Email-kalanidhimurugan%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" />
</a>

</div>

---

# ⭐ Support

If you find this project useful:

⭐ **Star the repository**

🍴 **Fork the project**

🐛 **Report issues**

💡 **Suggest improvements**

🤝 **Contribute**

---

<div align="center">

### 🧠 Turning Research Papers into Conversations

**Built with Python • FastAPI • Streamlit • RAG • Vector Search • LLMs**

⭐ **If you like this project, consider giving it a star!** ⭐

</div>
