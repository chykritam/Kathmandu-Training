# # 19th April 2026

# # For Loop in Python
# # Loops in list
# for i in [1, 2, 3, 4, 5, 1]:
#     print(i)
#     print("KMC")


# for i in [12, 21, 3, 44, 5, 1]:
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")


# # loop in string
# for i in "KMC":
#     print(i)


# # loop in dictionary
# a = {
#     "name": "Manish",
#     "collage": "Sarada",
# }
# for i in a:
#     # print(i) # it will print only key of the dictionary
#     # print(a[i]) # it will print value of the dictionary
#     print(f"{i} : {a[i]}")  # it will print key and value of the dictionary in one line


# for i in a.values():
#     print(i)  # it will print only value of the dictionary

# for i in a.keys():
#     print(i)  # it will print only key of the dictionary

#     # Range function
# for i in range(1, 10, 1):
#     print(i)  # it will print number from 1 to 9 with step of 1


# even = []
# odd = []
# for i in range(100, 200, 1):
#     if i % 2 == 0:
#         even.append(i)

#     else:
#         odd.append(i)
# print(even)
# print(odd)

# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     if i == 5:
#         break  # it will stop the loop when i is equal to 5
#     print(i)

# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     if i == 5:
#         continue  # it will skip the iteration when i is equal to 5
#     print(i)


# integers = []
# floats = []
# strings = []
# booleans = []

# for i in [1, 2, 3, 4, "Hello", "test", 1, 2, 4, 7.3, True]:
#     if type(i) == int:
#         integers.append(i)
#     elif type(i) == float:
#         floats.append(i)
#     elif type(i) == str:
#         strings.append(i)
#     elif type(i) == bool:
#         booleans.append(i)
# print(integers)
# print(floats)
# print(strings)
# print(booleans)

# # now we will do the same thing with isinstance() function
# integers = []
# floats = []
# strings = []
# booleans = []
# for i in [1, 2, 3, 4, "Hello", "test", 1, 2, 4, 7.3, True]:
#     if isinstance(i, int):
#         integers.append(i)
#     elif isinstance(i, float):
#         floats.append(i)
#     elif isinstance(i, str):
#         strings.append(i)
#     elif isinstance(i, bool):
#         booleans.append(i)
# print(integers)
# print(floats)
# print(strings)
# print(booleans)


# a = [10, 20, 30, 40]
# # not recommended while learning loop
# print(sum(a))  # it will print the sum of all the elements in the list a

# # recommended while learning loop
# total = 0
# for i in a:
#     total += i  # Same as total = total + i.
# print(
#     total
# )  # it will print the sum of all the elements in the list a by using for loop


# Nested for loop
for i in [1, 2, 3]:
    for j in [4, 5, 6, 7]:
        print(i, j)  # it will print all the combinations of i and j


print("................." * 20)


# while loop
while True:
    data = input("Enter a word: ")
    if data == "stop":
        break
    print(data)


# i=1
# while (i==1):
#   print(i)
#   i=3





# Question:

