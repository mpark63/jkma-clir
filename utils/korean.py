# script to confirm unicode to hangul
from unidecode import unidecode
import json
import os 
import shutil

# Path to the JSON file
folder_path = '/Users/mpark/Desktop/kclir_jsons'
cid_path = '/Users/mpark/Desktop/kclir_jsons/cid'
uni_path = '/Users/mpark/Desktop/kclir_jsons/unicode'

def unicode_to_korean(file_path): 
    with open(file_path, 'r', encoding='utf8') as json_file:
        try:
            s = json.load(json_file)
            with open(file_path, 'w', encoding='utf8') as json_file:
                json.dump(s, json_file, ensure_ascii=False, indent=4)
        except: 
            print(file_path)

def cid_to_korean(file_path):
    with open(file_path, 'r', encoding='utf8') as json_file:
        s = json.load(json_file)
        print (unidecode(s['symbols']))
    # with open(file_path, 'w', encoding='utf8') as json_file:
    #     json.dump(s, json_file, ensure_ascii=False, indent=4)
    

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if the current item is a file
    if os.path.isfile(file_path):
        # Do something with the file, for example, print its name
        unicode_to_korean(file_path)
        shutil.move(file_path, uni_path)

print('done')
