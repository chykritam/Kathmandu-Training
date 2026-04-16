#del
#remove
#pop
#clear

#using del keyword to remove elements of a list
a=[1,2,3,4,5]
del a[0]  # removes the first element of the list
print(a)

#using remove method to remove elements of a list
a=[1,2,3,4,5]   
a.remove(2)  # removes the first occurrence of the element 2 from the list
print(a)

#using pop method to remove elements of a list
a=[1,2,3,4,5]   
a.pop(0)  # removes the first element of the list and returns it
print(a)



#using clear method to remove all elements of a list
a=[1,2,3,4,5]   
a.clear()  # removes all elements of the list
print(a)
