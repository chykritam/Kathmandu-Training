# json String
import json

person ={
    "name": "Ram",
    "age": 22,
    "address": "KTM",
    "skills": ["python","Djangp","Machine Learnig"],
    "is_Programmer": True,
    "Phone": None
    }
person_json = json.dumps(person) # Dictionary => json String
print(person_json, type(person_json))




import json
json_string = """
{"name": "Ram", 
"age": 22, 
"address": "KTM", 
"skills": ["python", 
"Djangp", "Machine Learnig"], 
"is_Programmer": true, 
"Phone": null
}"""

x= json.loads(json_string)
print(x,type(x))




# import json

# person ={
#     "name": "Ram",
#     "age": 22,
#     "address": "KTM",
#     "skills": ["python","Djangp","Machine Learnig"],
#     "is_Programmer": True,
#     "Phone": None
#     }
# person_json = json.dumps(person) # Dictionary => json String
# with open("person.json","w") as f:
#     f.write(person_json) # Just write it, no need to print!
    
# print("File saved successfully!") # Add your own friendly message instead



import json

person ={
    "name": "Ram",
    "age": 22,
    "address": "KTM",
    "skills": ["python","Djangp","Machine Learnig"],
    "is_Programmer": True,
    "Phone": None
    }
person_json = json.dumps(person) # Dictionary => json String
with open("person.json","w") as f:
    json.dump(person,f, indent=4)

with open("person.json","r") as f:
    data =f.read()
    json_data = json.loads(data)
    print(json_data, type(json_data))



with open("Day 17/sample_users.csv","r") as f:
    print(f.read)


import  csv
with open("Day 17/sample_users.csv","r") as f:
    data = csv.DictReader(f)
    for i in data:
        print(i["first_name"],i["address"])




import csv
student= ("Ramesh", "Kathmandu",22)

with open("Day 17/student.csv", "w", newline='') as f:    
    writer = csv.writer(f)
    writer.writerow(student)



import csv

# 1. Create a bulk list of students (A List of Tuples)
bulk_data = [
    ("Ramesh", "Kathmandu", 22),
    ("Sita", "Pokhara", 21),
    ("Hari", "Lalitpur", 24),
    ("Gita", "Bhaktapur", 20)
]

# 2. Open the file 
# (Use "w" to create a new file, or "a" to add to an existing file)
with open("Day 17/bulk_students.csv", "w", newline='') as f:
    writer = csv.writer(f)
    
    # 3. Use the plural 'writerows' to dump the whole list at once!
    writer.writerows(bulk_data)

print("Bulk data saved successfully!")










import csv

# 1. Create a bulk list of students (A List of Tuples)
bulk_data = [
    ("Ramesh", "Kathmandu", 22),
    ("Sita", "Pokhara", 21),
    ("Hari", "Lalitpur", 24),
    ("Gita", "Bhaktapur", 20)
]

# 2. Open the file 
# (Use "w" to create a new file, or "a" to add to an existing file)
with open("Day 17/bulk_students_dictionary.csv", "w", newline='') as f:
    writer = csv.writer(f)
    
    # 3. Use the plural 'writerows' to dump the whole list at once!
    writer.writerows(bulk_data)

print("Bulk data saved successfully!")











