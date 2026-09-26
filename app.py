"""
Research Paper Answer Bot - Main Entry Point

This file can run either the FastAPI backend or the Streamlit frontend.
Usage:
  python app.py backend    # Run FastAPI backend
  python app.py frontend   # Run Streamlit frontend
  python app.py            # Run both (not recommended on Windows)
"""
import os
import sys
import argparse

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.config import load_config


def run_backend():
    """Run the FastAPI backend server."""
    import uvicorn
    from backend.main import app
    
    config = load_config()
    print(f"Starting FastAPI backend on {config.HOST}:{config.PORT}")
    uvicorn.run(app, host=config.HOST, port=config.PORT)


def run_frontend():
    """Run the Streamlit frontend."""
    import subprocess
    
    config = load_config()
    print("Starting Streamlit frontend...")
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
        "--server.port", "8501",
        "--server.address", "0.0.0.0",
    ])


def run_ingestion():
    """Run the ingestion pipeline for all PDFs in data/pdfs."""
    from services.pipeline import IngestionService
    
    config = load_config()
    ingestion = IngestionService(config)
    
    print("Starting ingestion pipeline...")
    chunks = ingestion.index_all_pdfs()
    print(f"Ingestion complete. {len(chunks)} chunks created.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Research Paper Answer Bot")
    parser.add_argument("mode", nargs="?", default="frontend",
                        choices=["backend", "frontend", "ingest"],
                        help="Run mode: backend, frontend, or ingest")
    
    args = parser.parse_args()
    
    if args.mode == "backend":
        run_backend()
    elif args.mode == "frontend":
        run_frontend()
    elif args.mode == "ingest":
        run_ingestion()