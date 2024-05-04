# script to extract title, author, and keyword from papermage metadata 
# when multiple options available, pick the longest one
import os
import json

def pick_longest(li):
  longest = ""
  for l in li:
      if len(l) > len(longest):
          longest = l
  return longest
json_folder = '/Users/mpark/Desktop/pageJsons/'
title_folder = '/Users/mpark/Desktop/titleJsons/'
new_folder = '/Users/mpark/Desktop/newJsons/'
count = 0

for filename in os.listdir(title_folder):
    title_path = os.path.join(title_folder, filename)
    json_path = os.path.join(json_folder, filename)
    new_path = os.path.join(new_folder, filename)
    if not os.path.isfile(title_path) or not os.path.isfile(json_path):
      continue

    # Load data from JSON file
    try: 
      with open(title_path, 'r', encoding='utf8') as file:
        metadata = json.load(file)
        # Insert data into Elasticsearch
        titles = metadata['titles']
        authors = metadata['authors']
        keywords = metadata['keywords']

      with open(json_path, 'r', encoding='utf8') as file:
        data = json.load(file)
        data['title'] = pick_longest(titles)
        data['author'] = pick_longest(authors)
        data['keyword'] = pick_longest(keywords)
      
      with open(new_path, 'w+') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
      print(f"Error: {e}")
      print(filename)
      continue