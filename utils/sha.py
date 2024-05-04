## script to "decode" the hashed value of pdf urls 
## add the url to the json file
import hashlib
from scrapy.utils.python import to_bytes
import os
import json

json_folder = '/Users/mpark/Desktop/newJsons/'

# Open the file in read mode
with open('urls.txt', 'r') as file:
    for line in file:
      hashed = hashlib.sha1(to_bytes(line.strip())).hexdigest()
      json_path = os.path.join(json_folder, hashed + '.json')
      if not os.path.isfile(json_path):
        print(line)
        continue

      with open(json_path, 'r', encoding='utf8') as file:
        data = json.load(file)
      
      with open(json_path, 'w+') as file:
        data['url'] = line.strip()
        json.dump(data, file, ensure_ascii=False, indent=4)
