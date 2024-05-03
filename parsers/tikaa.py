#!/usr/bin/env python
import os
from tika import parser
import json
from io import StringIO
from bs4 import BeautifulSoup

json_folder = "/Users/mpark/Desktop/pageJsons/"
cid_folder = "/Users/mpark/Desktop/pageJsons/cid/"
hangeul_folder = "/Users/mpark/Desktop/pageJsons/hangeul/"
pdf_folder = "/Users/mpark/Desktop/full/"

def extract_text_from_pdf(filename):
    pdf_path = os.path.join(pdf_folder, filename)
    dest_path = os.path.join(json_folder, filename.replace('.pdf', '.json'))

    data = parser.from_file(pdf_path, xmlContent=True)

    pages_txt = []
    xhtml_data = BeautifulSoup(data['content'])
    for i, content in enumerate(xhtml_data.find_all('div', attrs={'class': 'page'})):
        # It's faster and safer to create a new buffer than truncating it
        _buffer = StringIO()
        _buffer.write(str(content))
        parsed_content = parser.from_buffer(_buffer.getvalue())

        # Add pages
        text = parsed_content['content'].strip()
        pages_txt.append(text)
    
    parsed = { 'pages': pages_txt, 'pdf': filename }

    print(dest_path)
    with open(dest_path, 'w+', encoding='utf8') as json_file:
        json.dump(parsed, json_file, ensure_ascii=False, indent=4)

for filename in os.listdir(pdf_folder):
    if filename == '.DS_Store':
        continue
    extract_text_from_pdf(filename)

print('done')