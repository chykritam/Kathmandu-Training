# class Math():
#     def __init__(self,a,b,c):
#         self.a= a
#         self.b= b
#         self.c= c
#         print(a,b,c)
#         print(" Tis is __init__ method")
#         return None   # This prints None without even writing this line because __init__ method always returns None
    
#     def add(self):
#         return self.a+ self.b+ self.c
       
# obj = Math(1,69,100)
# print(obj.add())




# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def multi(self):
#         return self.length * self.breadth


# obj = Rectangle(12, 8)
# print("The Area is", obj.multi())




class Student():
    def __init__(self,name, marks):
        self.name = name
        self.marks= marks
    
    def average(self):
       if len(self.marks)== 0:
           raise "Zerodivision Error"
           
       return sum(self.marks)/ len(self.marks)
    
    def grade(self):
        avg =self.average()
        if avg >= 80:
            return "A"
        elif avg >=60:
            return "B"
        else:
            return "C"
        
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Average:", self.average())
        print("Grade is: ", self.grade())

obj =Student("Kritam", [90,90,90,90])

obj.display()






