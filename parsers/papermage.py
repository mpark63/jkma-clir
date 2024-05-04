import os
from papermage.recipes import CoreRecipe
import json 

recipe = CoreRecipe()

pdf_folder = "<REPLACE_WITH_PDF_FOLDER_PATH>"
json_folder = "<REPLACE_WITH_JSON_FOLDER_PATH>"

def pdf_to_json(pdf_name, pdf_folder, json_folder):
    file_path = os.path.join(pdf_folder, pdf_name)
    dest_path = os.path.join(json_folder, pdf_name.replace('.pdf', '.json'))

    if os.path.isfile(dest_path):
        return

    doc = recipe.run(file_path)

    curr = {}
    curr['pdf'] = pdf_name
    curr['metadata'] = doc.metadata.to_json()
    curr['titles'] = [title.text for title in doc.titles]
    curr['authors'] = [author.text for author in doc.authors]
    curr['keywords'] = [key.text for key in doc.keywords]
    curr['pages'] = []

    for page in doc.pages:
        currPage = []
        for row in page.rows:
            currPage.append(row.text)
        curr['pages'].append(' '.join(currPage))

    with open(dest_path, 'w+', encoding='utf8') as json_file:
        json.dump(curr, json_file, ensure_ascii=False, indent=4)

for filename in os.listdir(pdf_folder):
    if filename == '.DS_Store':
        continue
    print(filename)
    pdf_to_json(filename, pdf_folder, json_folder)

print('done')
