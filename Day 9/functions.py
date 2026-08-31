# # First Tuple
# # Also a datatype

# # Set doesn't support the duplicates but the Tuple does
# # Tuple cannot change the data.
# # Set is Unordered
# # Tuple is ordered
# # Tuple is faster than List
# # Tuple is immutable
# # Tuple is used when we want to store the data which cannot be changed.
# # Tuple is defined by using parentheses () and the elements are separated by commas.
# # Example of Tuple


# # Set is uded to remove the duplicates from the list and to store the unique elements.


# a = (1, 2, 3, 4, 5)
# print(type(a))
# # print(a[4])

# b = list(a)  # Convert the tuple to a list
# b[0] = 100  # Change the first element of the list
# a = tuple(b)  # Convert the list back to a tuple
# print(a)


# # Set
# data = {1, 2, 3, 4, "Hello", "test", 5, 1, 1, 2, 3}
# print(data)  # It will remove the duplicates and print the unique elements


# # Funtion is a block of code which is used to perform a specific task.
# # Function is defined by using the def keyword followed by the function name and parentheses ().
# # The code inside the function is indented.
# # Two types of functions are there in Python:
# # 1. User Defined functions
# # 2. In Built-in functions


# # Function return is important
# # Multiple return is also possible in Python using tuple

# # In Built-in functions are the functions which are already defined in Python and we can use them directly.
# # Pydentic

# # def test():
# #     a=600
# #     print("This it value of a", a)
# #     return a
# # test()


# # def test():
# #     print("Dekh Dekh")
# #     return [ 1,2,3,45],[1,2]
# # print(test())


# def sum_of_list():
#     a = [1, 2, 3, 4, 5, 6]
#     total = 0

#     for i in a:
#         total = total + i
#     return total


# print(sum_of_list())


# # # Making above code dynamic by taking input from the user

# # def user_info():
# #     fname = input("Enter your first name: ")
# #     lname = input("Enter your last name: ")
# #     return fname, lname

# # print(user_info())


# # Making above code dynamic without taking input inside the function

# # def user_info(fname, lname):
# #     return fname, lname

# # fname = input("Enter your first name: ")
# # lname = input("Enter your last name: ")
# # print(user_info(fname, lname))


# def check_number(num):
#     if num % 2 == 0:
#         return "Even"

#     else:
#         return "Odd"


# result = check_number(10)
# print(result)

# result = check_number(11)
# print(result)


# def max_number(a):
#     max_num = a[0]
#     for num in a:
#         if num > max_num:
#             max_num = num
#     return max_num


# result = max_number([1, 2, 3, 55, 5, 6])
# print(result)


# # Class starts with the uppeer Case
# # Function start with the lower case


# def log_event(event_type, *args, **kwargs):
#     if not isinstance(event_type, str):
#         return "Event type should be string"

#     if len(args) <= 0:
#         return "Provide atleast one message"

#     if kwargs.get("priority") == "high":
#         kwargs["alert"] = True

#     return {"type": event_type,
#             "messages": list(args),
#             "meta": kwargs}


# print(
#     log_event(
#         1,
#         "name r is not defined",
#         "type error cannot add str and int",
#         timestamp="2022-02-02",
#         user="root",
#         priority="low",
#     )
# )

# print(
#     log_event(
#         "Success",
#         "name r is not defined",
#         "type error cannot add str and int",
#         timestamp="2022-02-02",
#         user="root",
#         priority="low",
#     )
# )

# print(
#     log_event(
#         "error",
#         timestamp="2022-02-02",
#         user="root",
#         priority="low",
#     )
# )

# print(
#     log_event(
#         "error",
#         "name r is not defined",
#         "type error cannot add str and int",
#         timestamp="2022-02-02",
#         user="root",
#         priority="high",
#     )
# )


# # Recursion Function
# # It is a function which calls itself until it reaches the base case

# def test():
#     print("This is the test function")
#     return test()
# test()  # It will give RecursionError: maximum recursion depth exceeded


# Rescursion i the Factorial of a number
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))

