"""
Streamlit entry point for Research Paper Answer Bot.
Run with: streamlit run streamlit_app.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Run the chat frontend
from frontend.chat import *