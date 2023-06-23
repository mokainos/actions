import json
from datetime import datetime
from datetime import date
filepath = 'issues_list.json'
with open(filepath, "r") as json_file:
    listObj = json.load(json_file)

print(type(datetime.now().strftime('%d/%m/%Y')))   
print(listObj)
print(date.today())
today = date.today()
for x in range(len(listObj)):
    d = json.loads(listObj[x]) 
    end_date = datetime.strptime(d['Change_End_Date'], '%d/%m/%Y').date()
    print(today > end_date)
    if today > end_date:
         listObj.pop(x)
         
with open(filepath, "w") as json_file:
  json.dump(listObj, json_file, indent=4)