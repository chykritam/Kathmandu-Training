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

# a = {
#     "Name": "Manish",
#     "Age": 25,
#     "Height": 5.9,
#     "City": "Kailali",
#     "City": "Dhangadhi",
#     "phone": [123, 456, 7890],
# }
# print(type(a))
# print(len(a))

# # print(a["Name"])
# # print(a["Age"])
# # print(a["Height"])
# # print(a["City"])

# # # string also has length called as number of characters in the string
# # print(len("Manish"))


# # using get method to access the values of a dictionary
# print(a.get("Name"))
# print(a.keys())
# print(a.values())
# print(a.items())


# # Printing 456 from the list of phone numbers
# print(a["phone"][1])  # this will print 456
# print(a.get("phone")[-1])  # this will also print 456


# #
# user_info = {
#     "name": "Manish",
#     "age": 25,
#     "city": "Dhangadhi",
#     "phone": [123, 456, 7890],
# }
# # user_info["name"] = "Suman"
# # user_info["phone"]=9999
# # print(user_info)


# user_info.update({"name": "Parmila", "phone": 696969, "email": "parmila@example.com"})
# print(user_info)


# data = {
#     "name": "Manish",
#     "age": 25,
#     "city": "Dhangadhi",
#     "phone": [123, 456, 7890],
#     "email": "manish@gmail.com",
# }
# print(data)
# del data["email"]  # this will remove the email key and its value from the dictionary
# print(data)

# data.pop() # this will remove the phone key and its value from the dictionary and return it
# print(data)


# # This will raise a KeyError because the dictionary is empty and there is no item to pop. But it will print anyway because we are printing the dictionary after popping the item.
# k = {}
# a.popitem()
# print(k)


# # Dictionary with nested list and dictionary
# # Question:
# user_info = {
#     "name": "Manish",
#     "age": 25,
#     "city": "Dhangadhi",
#     "phone": [
#         {"type": "NTC", "number": 1234567890},
#         {"type": "Ncell", "number": 9876543210},
#         {"type": "SmartCell", "number": 5555555555},
#     ],
# }
# # the output should be Manish NTC number is 1234567890.
# print(
#     f"{user_info['name']}  {user_info['phone'][0]['type']} number is {user_info['phone'][0]['number']}."
# )


# # The output should be Manish Ncell number is 9876543210.
# print(
#     f"{user_info['name']} {user_info['phone'][1]['type']} number is {user_info['phone'][1]['number']}."
# )



# Nested Dictionary
user_info = {
    "name": "Manish",
    "address" :{
        "temp": "Bhaktapur",
        "permanent": "Kailali",
    }
    },
print(user_info)
print(f"{user_info['address']['temp']}")  # this will print Bhaktapur
print(f"{user_info['address']['permanent']}" )  # this will print Kailali
      

