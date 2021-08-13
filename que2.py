import json

dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
} 

for i in dict1['emp2']:
    print(dict1['emp2'][i])
    
# out_file = open("myfile.json", "w")

# json.dump(dict1, out_file, indent = 6)

# out_file.close() 