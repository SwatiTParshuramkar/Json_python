import json
# a Python object (dict):
python_obj = {
  "name": "Swati",
  "Blood Group":"A-Ve",
  "age": 45  
}
print(type(python_obj))
# convert into JSON:
j_data = json.dumps(python_obj)

# result is a JSON string:
print(j_data)
