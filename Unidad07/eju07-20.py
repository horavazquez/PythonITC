import json

sampleJson="""
{ 
    "company": {
        "name": "International INC", 
        "employees": [
            { 
            "name":"emma",
            "payable": { 
                "salary":7000,
                "bonus":800
                }
            },
            { 
            "name":"john",
            "payable": { 
                "salary":6000,
                "bonus":2000
                }
            },
	        { 
            "name":"jane",
            "payable": { 
                "salary":8000,
                "bonus":0
                }
            }
        ]
    }
}
"""

try:
    data = json.loads(sampleJson)
except Exception as e:
    print(e)

print("Empresa: ", data['company']['name'])

for i, emp in enumerate(data['company']['employees'],start=1):
    print(i, "= Empleado: ", emp.get('name'), "- Salario: ", emp['payable']['salary'])
    
