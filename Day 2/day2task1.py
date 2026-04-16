name = "Manish"
age = 19
address = "Dhangadhi"

print("My name is", name, "My age is", age, " My address is", address)
print("My name is {} My age is {} My address is {}".format(name, age, address))
print(
    f"My name is {name} My age is {age} My address is {address}"
)  # best way to print the data
print("My name is %s My age is %d My address is %s" % (name, age, address))
print("My name is " + name + " My age is " + str(age) + " My address is " + address)
