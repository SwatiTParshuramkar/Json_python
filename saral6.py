import json
python_obj = '{ "a": 1,"a" : 2,"a" : 3,"c":9,"a": 4,"b": 1, "b": 2 ,"c":8}'
print("Original Python object:")
print(python_obj)
json_obj = json.loads(python_obj)
print("\nUnique Key in a JSON object:")
print(json_obj)