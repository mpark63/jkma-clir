# This script reads JSON files from a folder and ingests them into Elasticsearch
# Update .env file (see .env.example) 
# Install elastisearch: python -m pip install elasticsearch
# Run the file in command line: python elasticsearch.py

from time import sleep
from elasticsearch import Elasticsearch
import os 
import json

client = Elasticsearch(
  os.environ["ELASTICSEARCH_ENDPOINT"],
  api_key=os.environ["ELASTICSEARCH_APIKEY"]
)

documents = []
json_folder = os.environ["JSON_FOLDER_PATH"]
count = 0
for filename in os.listdir(json_folder):
    file_path = os.path.join(json_folder, filename)
    if not os.path.isfile(file_path):
      continue

    # Load data from JSON file
    try: 
      with open(file_path, 'r') as file:
        data = json.load(file)
        # Insert data into Elasticsearch
        documents.append({ "index": { "_index": os.environ["ELASTISEARCH_INDEX"], "_id": filename.replace('.json', '')}})
        documents.append(data)
    except Exception as e:
      print(f"Error: {e}")
      print(filename)
      continue

    count += 1

    # bulk index documents every 50 documents 
    try: 
      if count % 50 == 0:
        client.bulk(operations=documents, pipeline="ent-search-generic-ingestion")
        documents = []
        print(f"Indexed {count} documents")
    except Exception as e:
      print(f"Error: {e}")
      break

# index remaining documents
if len(documents) > 0:
  client.bulk(operations=documents, pipeline="ent-search-generic-ingestion")

print(f"Indexed {count} documents")
print("Done indexing")