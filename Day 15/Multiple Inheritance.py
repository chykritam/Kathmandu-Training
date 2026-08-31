# class Parent1:
#     a = 10
#     b = 11


# class Parent2:
#     a = 100
#     b = 10


# class Child(Parent1, Parent2):
#     a = 2


# obj = Child()
# print(obj.a)
# print(Child.__mro__)




# # Normal vs Lambda function


# def add(a,b)
#     return a+b
# add(1,5)

# add= lambda x,y: x+y
# print(add(1,5))




# # list Comprehension with Lambda Function
# data =[1,2,3,4]
# a=[i**2 for i in data]
# print(a)




# square= lambda*args:[i**2 for i in args]
# print(square(1,2,3,4,5))
# print(square(15,26))



# generate_list = lambda n: [x for x in range(1, n + 1)]
# my_numbers = generate_list(5)
# print(my_numbers)


# class A():
#     __a = 1
#     b = __a +1
#     obj = __a+1

#     def __add(self):
#         return self.__a + self.b
    

#     def public.add(self):
#        return self.__add() 


# print(obj)






class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def show_balance(self):
        return self.__balance

class StudentAccount(BankAccount):
    def __init__(self, account_holder, balance, student_id):
        super().__init__(account_holder, balance)
        self.student_id = student_id

    def pay_library_fine(self, amount):
        self._BankAccount__balance -= amount
        print(self.show_balance())

account1 = BankAccount("Ram Thapa", 5000)
print(account1.account_holder)
account1.deposit(1000)
print(account1.show_balance())

student1 = StudentAccount("Sita Sharma", 3000, "S-101")
print(student1.account_holder)
print(student1.student_id)
student1.deposit(500)
student1.pay_library_fine(200)
print(student1.show_balance())




# school management system banaudai chau bhanera assume ggara.


#inheritance use garera tala ko requirenment pura garne program lekah  base class BankAccount: public sttributr account holder privstr attribute balance, public methons: deposit(amount)  show(Balance)
# Derive Class Student accoount
# public attribute studentID  pau>Librarygine(amount) method banaune jasle direct balance access garna khoojos fine amount ghatauna khojos  baki balance print garos
# Tasks.   duita clss ko object banaune
# sabai possiblr public members access  garne. 
#present balance accesss garna etc etc



class BankAccount():
    account_Holder="Kritam Chaudhary"
    __balance=5000

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
    def show_balance(self):
        return self.__balance
class StudentAccount(BankAccount):
    studentID="S-101"
    def pay_library_fine(self,amount):
        self._BankAccount__balance-=amount
        print(self.show_balance())
account1=BankAccount()
print(account1.account_Holder)
account1.deposit(1000)
print(account1.show_balance())
student1=StudentAccount()
print(student1.account_Holder)
print(student1.studentID)
student1.deposit(500)
student1.pay_library_fine(200)
print(student1.show_balance())


#where is withdraw method? where is balance check method? where is transfer method? where is interest calculation method? where is loan application method? where is account closure method? where is account statement method? where is customer support method? where is online banking method? where is mobile banking method? where is ATM access method? where is fraud detection method? where is financial planning method? where is investment advice method? where is retirement planning method? where is tax consultation method? where is insurance services method? where is credit score monitoring method? where is budgeting tools method? where is financial education resources method?

# Sir le Gsreko Program

class BankAccount:
    account_holder = "Kritam Chaudhary"
    __balance = 5000

    def withdraw(self, amount):
        self.__balance -= amount
        return amount
    
    def deposit(self, amount):
        self.__balance += amount
        return amount
    
    def show_balance(self):
        return self.__balance
    


class StudentAccount(BankAccount):
    student_id = "S-101"



    def paylibrary_fine(self, amount):
        reurn self.withdraw(amount)

account1 = BankAccount()
print(account1.account_holder)
account1.deposit(1000)
print(account1.show_balance())
    
     




    
   




