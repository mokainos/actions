
import json
import os

listObj = []
filepath = 'issues_list.json'
new_data = os.environ["NEW_DATA"]
print(new_data)
try:
  with open(filepath, "r") as json_file:
    listObj = json.load(json_file)
except FileNotFoundError:
  with open(filepath, "w") as json_file:
    listObj.append(new_data)
    json.dump(listObj, json_file, indent=4)
else:
  listObj.append(new_data)
  with open(filepath, "w") as json_file:
    json.dump(listObj, json_file, indent=4)

