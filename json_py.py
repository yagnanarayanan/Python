import json
data = '{"Name":"Shyam", "Age":14, "Voter":false}'
parsed = json.loads(data)
print(parsed)
print(type(parsed))
# parsed data is a dictionary
data1 = {"Name": "Shyam", "Age": 14, "Voter": False, "Things": (23, "eat")}
js = json.dumps(data1)
print(js)
# dumped data is JS compatible object
print(type(data1))
