import json  
    
# JSON string:  
# Multi-line string  
data = """{  
    "Name": "Jennifer Smith",  
    "Contact Number": 7867567898,  
    "Email": "jen123@gmail.com",  
    "Hobbies":["Reading", "Sketching", "Horse Riding"]  
    }"""
    
# parse data:  
res = json.loads( data )  
    
# the result is a Python dictionary:  
print( res["Hobbies"][0] )