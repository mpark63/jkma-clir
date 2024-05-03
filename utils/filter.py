import os
import shutil

json_folder = "/Users/mpark/Desktop/pageJsons/"
cid_folder = "/Users/mpark/Desktop/pageJsons/cid/"
hangeul_folder = "/Users/mpark/Desktop/pageJsons/hangeul/"

def filter(filename):
    file_path = os.path.join(json_folder, filename)

    if not os.path.isfile(file_path):
        return

    with open(file_path, 'r', encoding='utf8') as file:
        file_contents = file.read()
        # Check if the target string occurs in the file contents
        count = file_contents.count('(cid:')
        if count > 100: 
            shutil.move(json_folder+filename, cid_folder+filename)
        else: 
            shutil.move(json_folder+filename, hangeul_folder+filename)

for filename in os.listdir(json_folder):
    if filename == '.DS_Store':
        continue
    print(filename)
    filter(filename)

print('done')
