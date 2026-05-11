# class Person:
#     a = 100
#     b = 1000


# data = Person()
# # Printing attributes of classs with the objects
# print(data.a)
# data.door = "main door"
# print(data.door)
# data2 = Person()


# class Test:
#     a = " Kritam"
#     b = " Chaudhary"

#     def add(hari):
#         return hari.a + hari.b

# obj1 = Test()
# print(obj1.a)
# print(obj1.add())


class Persons:
    b = 100

    def test(self):
        self.a = 23
        print(self.a)
        print("This is class attribute", self.a)
        return self.a

    def multi(self):
        return self.test() * self.b


obj = Persons()
print(obj)

# initialize a first (otherwise multi() fails)
obj.test()

print(obj.multi())
print(obj.a)




