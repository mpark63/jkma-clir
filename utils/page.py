## script to populate the number of pages in the json files
import os
import json
import PyPDF2

pdf_folder = "/Users/mpark/Desktop/full/"
json_folder = "/Users/mpark/Desktop/pageJsons/"

def num_pages(filename):
    file_path = os.path.join(json_folder, filename)
    pdf_path = os.path.join(pdf_folder, filename.replace('.json', '.pdf'))

    if not os.path.isfile(file_path):
        return
    
    
    obj = json.load(open(file_path))
    num_p = len(obj['pages'])

    # opened file as reading (r) in binary (b) mode
    file = open(pdf_path, 'rb')
    # store data in pdfReader
    pdfReader = PyPDF2.PdfReader(file)
    assert num_p == len(pdfReader.pages)

    obj['num_pages'] = num_p

    with open(file_path, 'w+', encoding='utf8') as json_file:
        json.dump(obj, json_file, ensure_ascii=False, indent=4)

for filename in os.listdir(json_folder):
    if filename == '.DS_Store':
        continue
    num_pages(filename)
    print(filename)

print('done')
