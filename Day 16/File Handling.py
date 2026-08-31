a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
add_ten = lambda x: x + 10
a = [add_ten(num) for num in a]
print(a)



f = open("hello.txt","w")
f.write("hello World!")
f.close 


f= open("hello.txt","r")
print(f.read())
f.close





# Error Handling



#Zero Division error
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
print(divide(10, 2)) 


def division(a,b):
    try:
        result= a/b
        return result
    except ZeroDivisionError :
        print("Faaaaaaah!")
print(division(6,0))


#Type error
def division(a,b):
    try:
        result= a/b
        return result
    except ZeroDivisionError :
        print("Faaaaaaah!")
    except TypeError:
        print("Invalid Faaaah!")
    except Exception as e:
        print(e)
print(division(1,1))







# Any Kind of error
def division(a,b):
    try:
        result= a/b
        return result

    except Exception as e:
        print(e)
print(division(1,0))

#Using else
def division(a,b):
    try:
        result= a/b
        
    except ZeroDivisionError :
        print("Faaaaaaah!")
    except TypeError:
        print("Invalid Faaaah!")
    except NameError:
        print("hello")
    except Exception as e:
        print(e)
    else: 
        print("I will run if no error")
        return result
print(division(11,a))






# # The following code will raise an exception because of division by zero. The line `print("Hi")` will not be executed due to the exception.
print("hello")




with open("hello.txt","w")as f:
    f.write("Hello World" \
    "hzdifjidjfidjsfidsj" \
    "efdsfjdsdjfdsijioljgisjgi" \
    "fdfjdkfjdkjfidsjfidsjfij")
print(f.close)




with open("hello.txt")as f:
    print(f.closed)
    print(f.read())
    print(f.closed)

print(f.closed)


# #didn't Work
# with open("hello.txt")as f:
#     print(f.closed)
#     print(f.read())
#     1/0

# print(f.close) 


with open("hello.txt" ,"r")as f:
   
    print(f.read())



with open("hello.txt","r") as f:
    print(f.read(10)) #read first 10 Characters
    print(f.tell())



with open("hello.txt","r") as f:
    print(f.read(10)) #read first 10 Characters
    print(f.tell())
    f.seek(0)
    print(f.tell())


with open("hello.txt","r") as f:
   f.seek(1)
   print(f.read(4))




with open("Day 16/python.jpeg", "rb") as f:
    print(f.read())

