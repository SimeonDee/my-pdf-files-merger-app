import os
import streamlit as st

# app = Flask(__name__)

sidebar = st.sidebar

sidebar.page_link('pages/merge_pdf_files.py', label='Merge PDF Files', icon="🏠")
sidebar.page_link('pages/reduce_pdf_size.py', label='Reduce PDF Size')

st.title('Welcome to PDF Utilities Site')
st.markdown("""
---
_**Author:**_ `Adeyemi Adedoyin Simeon`

---
""")

st.title('This provide you with the ability to merge Multiple PDF files as well as reduce large PDF file size')
st.page_link('pages/merge_pdf_files.py', label='Merge PDF Files')
st.page_link('pages/reduce_pdf_size.py', label='Reduce PDF Size')
