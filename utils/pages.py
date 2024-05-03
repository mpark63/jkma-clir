import os 
import json 
from copy import deepcopy 

json_folder = '/Users/mpark/Desktop/newJsons/'
page_folder = '/Users/mpark/Desktop/pageJsons/'

for filename in os.listdir(json_folder):
  json_path = os.path.join(json_folder, filename)
  if not os.path.isfile(json_path):
    continue
  with open(json_path, 'r', encoding='utf8') as file:
    data = json.load(file)
    curr = deepcopy(data)
    del curr['pages']
    for i, page in enumerate(data['pages']):
      curr['text'] = page
      curr['pageNumber'] = i + 1
      page_path = os.path.join(page_folder, filename.replace('.json', '')+ '-' + str(i+1)+'.json')
      with open(page_path, 'w+') as file:
        json.dump(curr, file, ensure_ascii=False, indent=4)
      print(page_path)