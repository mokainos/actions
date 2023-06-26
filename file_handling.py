
import json
import os
from datetime import datetime
from datetime import date

listObj = []
listObjwrite = []
filepath = 'issues_list.json'
new_data = os.environ.get('NEW_DATA')
today = date.today()
print(today)
print(new_data)
try:
  with open(filepath, "r") as json_file:
    listObj = json.load(json_file)
except FileNotFoundError:
  with open(filepath, "w") as json_file:
    listObjwrite.append(new_data)
    json.dump(listObjwrite, json_file, indent=4)
else:
  print(len(listObj))
  print(type(listObj))
  print(listObj)
  listObjwrite = []
  for x in range(len(listObj)):
    print("================")
    print(x)
    d = listObj[x] 
    print(type(d))
    print(d)
    
    if d['Skip shutdown end date'] == "_No response_":
      
      d['Skip shutdown end date'] = today.strftime('%d-%m-%Y')
      print(d)
      listObjwrite.append(d)
      print(listObjwrite)
    else:
      end_date = datetime.strptime(d['Skip shutdown end date'], '%d-%m-%Y').date()
      print( end_date)
      if today < end_date:
        listObjwrite.append(d)
      print(listObjwrite) 
  if new_data:
    listObjwrite.append(new_data)
  print("before write")  
  print(listObjwrite)
  with open(filepath, "w") as json_file:
    json.dump(listObjwrite, json_file, indent=4)

