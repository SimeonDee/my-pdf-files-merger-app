import streamlit as st
from pypdf import PdfReader, PdfWriter
from werkzeug.utils import secure_filename
import os

UPLOADS_FOLDER = 'uploads'
SUPPORTED_FILES = ['pdf']
writer = PdfWriter()
DEST_FOLDER = 'destination'

if not os.path.exists(UPLOADS_FOLDER):
    os.mkdir(UPLOADS_FOLDER)

if not os.path.exists(DEST_FOLDER):
    os.mkdir(DEST_FOLDER)

st.title('PDF File Size Reducer')
st.markdown("""
---
_**Author:**_ `Adeyemi Adedoyin Simeon`

---
""")

ct = st.container(border=True)

uploaded_file = ct.file_uploader('Upload Your PDF file', type=SUPPORTED_FILES, accept_multiple_files=False)
reduced_file_name = ct.text_input('Reduced file download name', value='ReducedPDF.pdf')
reduce_btn = ct.button('Reduce Size', type='primary', use_container_width=True)

if reduce_btn:
    if reduced_file_name == '':
        reduced_file_name = 'ReducedPDF.pdf'
    elif not reduced_file_name.endswith('.pdf'):
        reduced_file_name += '.pdf'

    if uploaded_file is None or uploaded_file == '':
        ct.error('Please upload a file')
    else:
        if uploaded_file.name.split('.')[1] in SUPPORTED_FILES:
            save_path = f'{UPLOADS_FOLDER}/{secure_filename(uploaded_file.name)}'
            with open(save_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())

        reader = PdfReader(save_path)

        for page in reader.pages:
            writer.add_page(page)

        if reader.metadata is not None:
            writer.add_metadata(reader.metadata)

        with open(f'{DEST_FOLDER}/{reduced_file_name}', "wb") as fp:
            writer.write(fp)
        
            ct2 = st.container(border=True)
            ct2.success('File reduced successfully. You can now download the reduced file')
        
        with open(f'{DEST_FOLDER}/{reduced_file_name}', "rb") as fp:
            ct2.download_button(
                label='Download reduced file', 
                data=fp.read(), 
                mime="application/pdf", 
                file_name=reduced_file_name, 
                type='primary')