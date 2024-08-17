import pypdf as pp
import os
from werkzeug.utils import secure_filename
import streamlit as st


# # PDF Merger
merger = pp.PdfWriter()
UPLOADS_FOLDER = 'uploads'
DEST_FOLDER = 'merges'
SUPPORTED_FILES = ['pdf']

if not os.path.exists(UPLOADS_FOLDER):
    os.mkdir(UPLOADS_FOLDER)

if not os.path.exists(DEST_FOLDER):
    os.mkdir(DEST_FOLDER)


st.title('PDF Files Merger')
st.markdown("""
---
_**Author:**_ `Adeyemi Adedoyin Simeon`

---
""")

ct = st.container(border=True)
uploaded_files = ct.file_uploader('Upload your PDF files', type=SUPPORTED_FILES, accept_multiple_files=True)
merged_filename = ct.text_input('Merged file name', value='CombinedPDFs.pdf')

merge_btn = ct.button('Merge Files', type='primary')

if merge_btn:
    # delete previous files for fresh entry
    for file in os.listdir(UPLOADS_FOLDER):
        os.remove(f'{UPLOADS_FOLDER}/{file}')
    
    for file in os.listdir(DEST_FOLDER):
        os.remove(f'{DEST_FOLDER}/{file}')

    if merged_filename == '':
        merged_filename = 'CombinedPDFs.pdf'

    if not uploaded_files or isinstance(uploaded_files, list) == False:
        ct.error('You need to upload at least two PDF files to merge', icon="🔥")
    elif len(uploaded_files) < 2:
        ct.error('You need to upload at least two PDF files to merge', icon="🔥")
    else:
        for file in uploaded_files:
            # if file.name.endswith('.pdf'):
            if file.name.split('.')[1] in SUPPORTED_FILES:
                save_path = f'{UPLOADS_FOLDER}/{secure_filename(file.name)}'
                with open(save_path, 'wb') as f:
                    f.write(file.getbuffer())

                merger.append(save_path)

        merger.write(f'{DEST_FOLDER}/{merged_filename}')

        ct2 = st.container(border=True)
        ct2.success('File merged successfully. You can now download the merged file')
        
        with open( f'{DEST_FOLDER}/{merged_filename}', 'rb') as f:
            ct2.download_button(
                label='Download merged file', 
                data=f.read(), 
                mime="application/pdf", 
                file_name=merged_filename, 
                type='primary')

