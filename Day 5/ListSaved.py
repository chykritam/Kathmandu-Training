# print("This is new file for github branch testing")

# list1 = [1, 2, 3, 4, 5, 6, 7]
# print(list1)

# print(list1[-1])  # last element of the list
# print(list1[-2])  # second last element of the list
# print(list1[0:3])  # first three elements of the list
# print(list1[3:])  # all elements from index 3 to the end of the list
# print(list1[:4])  # all elements from the beginning of the list to index
# print(list1[::2])  # all elements from the list with a step of 2
# print(list1[1::2])  # all elements from the list with a step of 2 starting from index 1
# print(list1[::-1])  # all elements from the list in reverse order
# print(list1[1:6:2])  # all elements from index 1 to index 5 with a step of 2
# print(list1[::3])  # all elements from the list with a step of 3
# print(list1[1:5:3])  # all elements from index 1 to index 4 with a step of 3
# print(list1[2:5:2])  # all elements from index 2 to index 4 with a step of 2
# print(list1[::4])  # all elements from the list with a step of 4
# print(list1[1:6:4])  # all elements from index 1 to
# print(list1[2:6:3])  # all elements from index 2 to index 5 with a step of 3
# print(list1[::5])  # all elements from the list with a step of 5
# print(list1[1:6:5])  # all elements from index 1 to
# print(list1[2:6:4])  # all elements from index 2 to index 5 with a step of 4


# list2 = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

# print(list2)
# print(list2[-1])  # last element of the list
# print(list2[-2])  # second last element of the list
# print(list2[0:3])  # first three elements of the list
# print(list2[3:])  # all elements from index 3 to the end of the list
# print(list2[:4])  # all elements from the beginning of the list to index 4
# print(list2[::2])  # all elements from the list with a step of
# print(list2[1::2])  # all elements from the list with a step of 2 starting from index 1
# print(list2[::-1])  # all elements from the list in reverse order
# print(list2[1:6:2])  # all elements from index 1 to
# print(list2[::3])  # all elements from the list with a step of 3
# print(list2[1:5:3])  # all elements from index 1 to index 4 with a step of 3
# print(list2[2:5:2])  # all elements from index 2 to index 4 with a step of 2
# print(list2[::4])  # all elements from the list with a step of 4
# print(list2[1:6:4])  # all elements from index 1 to index 5 with a step of 4
# print(list2[2:6:4])  # all elements from index 2 to index 5 with a step of 4
# print(list2[::5])  # all elements from the list with a step of 5
# print(list2[1:6:5])  # all elements from index 1 to index 5 with a step of 5
# print(list2[2:6:5])  # all elements from index 2 to index 5 with a step of 5

#using extend method to add elements of one list to another list

a=[1,2]
b=[3,4]
b.extend(a)
a.extend(b)
print(a)
print(b)


#using append method to add elements of one list to another list
a=[1,2]
b=[3,4]
b.append(a)
a.append(b)
print(a)
print(b)


#using insert method to add elements of one list to another list
a=[1,2]
b=[3,4]
b.insert(0,a)
a.insert(0,b)
print(a)
print(b)

#using + operator to add elements of one list to another list
a=[1,2]
b=[3,4]
a=a+b
print(a)
print(b)



#using * operator to add elements of one list to another list
a=[1,2]
b=[3,4]
a=a*2
print(a)
print(b)

#using list comprehension to add elements of one list to another list
a=[1,2]
b=[3,4]
a=[x for x in a]+[x for x in b]
print(a)
print(b)


#using map function to add elements of one list to another list
a=[1,2]
b=[3,4]
a=list(map(lambda x: x, a))+list(map(lambda x: x, b))
print(a)
print(b)





