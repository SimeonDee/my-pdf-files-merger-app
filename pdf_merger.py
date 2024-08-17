import PyPDF2 as pp
import os
# PDF Merger
merger = pp.PdfMerger()
for file in os.listdir('PDFs'):
    if file.endswith('.pdf'):
        merger.append(f'PDFs/{file}')

merger.write('merges/Combined.pdf')