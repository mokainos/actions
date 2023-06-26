
import json
import os
from datetime import datetime
from datetime import date

listObj = []
filepath = 'issues_list.json'
new_data = os.environ.get('NEW_DATA')
print("todays date")
today = date.today()
print(today)
print(type(today))
print(new_data)
try:
  with open(filepath, "r") as json_file:
    listObj = json.load(json_file)
except FileNotFoundError:
  with open(filepath, "w") as json_file:
    listObj.append(new_data)
    json.dump(listObj, json_file, indent=4)
else:
  print(len(listObj))
  listObjwrite = []
  for x in range(len(listObj)):
    print("================")
    print(x)
    d = json.loads(listObj[x]) 
    print(d)
    
    if d['Skip shutdown end date'] == "_No response_":
      end_date = today
      d['Skip shutdown end date'] = end_date
      print(listObj)
      listObjwrite.append(d)
    else:
      end_date = datetime.strptime(d['Skip shutdown end date'], '%d-%m-%Y').date()
      print( end_date)
      if today < end_date:
        listObjwrite.append(d)
            
  if new_data:
    listObjwrite.append(new_data)
  print("before write")  
  print(listObjwrite)
  with open(filepath, "w") as json_file:
    json.dump(listObjwrite, json_file, indent=4)

