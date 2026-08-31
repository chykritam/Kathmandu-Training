# Using Sort method to sort a list in ascending order
# Sort the list alphabetically
# The sort() method sorts the list ascending by default
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil','Haris', 'Ihsan']
teachers.sort()

# Sorts the list in descending
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil','Haris', 'Ihsan']
teachers.sort(reverse = True)
print(teachers)


# Using sorted function to sort a list in ascending order
# Sort the list alphabetically
# The sorted() function sorts the list ascending by default
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil','Haris', 'Ihsan']
sorted_teachers = sorted(teachers)
# Sorts the list in descending
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz',
            'Farhan', 'Khalil','Haris', 'Ihsan']
sorted_teachers = sorted(teachers, reverse = True)
print(sorted_teachers)
