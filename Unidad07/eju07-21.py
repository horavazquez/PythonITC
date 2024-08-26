import json

sampleJson = """ 
[
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]
"""

data = {}
try:
    data = json.loads(sampleJson)
except Exception as e:
    print(e)
#dataList=[]
#dataList = [item.get('color') for item in data]
print (data)
for item in data.keys():
    print (item)
    """for n in item.get('name'):
        print(n.get('color'))
"""

#print(dataList) # type: ignore