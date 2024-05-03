from time import sleep
from elasticsearch import Elasticsearch
import os 
import json

client = Elasticsearch(
  os.environ["ELASTICSEARCH_ENDPOINT"],
  api_key=os.environ["ELASTICSEARCH_APIKEY"]
)

documents = []
json_folder = '/Users/mpark/Desktop/pageJsons/'
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
        documents.append({ "index": { "_index": "jkma-pages-json", "_id": filename.replace('.json', '')}})
        documents.append(data)
    except Exception as e:
      print(f"Error: {e}")
      print(filename)
      continue

    count += 1

    # load 10 and reset 
    try: 
      if count % 50 == 0:
        client.bulk(operations=documents, pipeline="ent-search-generic-ingestion")
        documents = []
        print(f"Indexed {count} documents")
    except Exception as e:
      print(f"Error: {e}")
      break

if len(documents) > 0:
  client.bulk(operations=documents, pipeline="ent-search-generic-ingestion")

print(f"Indexed {count} documents")
print("Done indexing")

# results = client.search(index="jkma-pages", q="우울증")
# print(results)