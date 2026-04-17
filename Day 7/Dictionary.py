# # Create a dictionary of boy details
# boy = {
#         'Name': 'Ali',
#         'Age': 21,
#         'Height': 6,
#         'Weight': 68,
#         'City':'Peshawar',
#         'Religion': 'Muslim'
#     }
# print(boy)
# {
#     'Name': 'Ali',
#     'Age': 21,
#     'Height': 6,
#     'Weight': 68,
#     'City':'Peshawar',
#     'Religion': 'Muslim'
# }

a = {
    "Name": "Manish",
    "Age": 25,
    "Height": 5.9,
    "City": "Kailali",
    "City": "Dhangadhi",
    "phone": [123, 456, 7890],
}
print(type(a))
print(len(a))

# print(a["Name"])
# print(a["Age"])
# print(a["Height"])
# print(a["City"])

# # string also has length called as number of characters in the string
# print(len("Manish"))


# using get method to access the values of a dictionary
print(a.get("Name"))
print(a.keys())
print(a.values())
print(a.items())


# Printing 456 from the list of phone numbers
print(a["phone"][1])  # this will print 456
print(a.get("phone")[-1])  # this will also print 456


# 
user_info={
    "name": "Manish",
    "age": 25,
    "city": "Dhangadhi",
    "phone": [123, 456, 7890],
}
# user_info["name"] = "Suman"
# user_info["phone"]=9999
# print(user_info)



user_info.update({"name": "Parmila", "phone": 696969, "email": "parmila@example.com"})
print(user_info)


