# class Parent():
#     a =45
#     b = 100

#     def add(self):
#        return self.a + self.b
    
# class Child(Parent):
#     d= 10
    
#     def display(self):
#         return self.add()
    
# obj = Child()
# print(obj.b)
# print(obj.a)
# print(obj.display())
    



# class TestParent():
#     def __init__(self):
#         print("I am From Test Parent")
    
# class TestChild(TestParent):
#     def __init__(self):
#         print("I am from test Child")
#         TestParent.__init__(self)
#         super().__init__()

# obj = TestChild()



# #Question

# class TestParent():
#     def __init__(self,a):
#         print("I am From Test Parent")
    
# class TestChild(TestParent):
#     def __init__(self,a,b,c,d):
#         print("I am from test Child")
#         self.b = b
#         TestParent.__init__(self,a)
#         super().__init__(a)

# class Child(TestChild): 
#     pass
# obj = TestChild(1,2,3,4)





# class Account:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance
#         self.transaction_history = []

#     def deposit(self, amount):
#         self.balance += amount
#         self.transaction_history.append(f"Deposited: {amount}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds")
#             return
#         self.balance -= amount
#         self.transaction_history.append(f"Withdrew: {amount}")
        
# class SavingsAccount(Account):
#     def __init__(self, account_number, balance, interest_rate):
#         super().__init__(account_number, balance)
#         self.interest_rate = interest_rate

#     def add_interest(self):
#         interest = self.balance * self.interest_rate
#         self.deposit(interest)

# class PremiumSavingsAccount(SavingsAccount):
#     def __init__(self, account_number, balance, interest_rate, reward_points):
#         super().__init__(account_number, balance, interest_rate)
#         self.reward_points = reward_points

#     def redeem_points(self):
#         if self.reward_points >= 100:
#             self.deposit(10)  # Redeem points for a $10 deposit
#             self.reward_points -= 100
#             print("Redeemed 100 points for $10")
#         else:
#             print("Not enough reward points to redeem")

#     def withdraw(self, amount):
#         if self.balance - amount < 50:  # Minimum balance condition
#             print("Cannot withdraw. Minimum balance of $50 must be maintained.")
#             return
#         super().withdraw(amount)
# # Example usage
# account = PremiumSavingsAccount("123456", 500, 0.05, 150)
# account.deposit(100)
# account.withdraw(200)
# account.add_interest()
# account.redeem_points()
# print("Final Balance:", account.balance)

# class Device:
#     def __init__(self, device_id):
#         self.device_id = device_id
#         self.status = "off"

#     def turn_on(self):
#         self.status = "on"
#         print(f"{self.device_id} is turned on.")

#     def turn_off(self):
#         self.status = "off"
#         print(f"{self.device_id} is turned off.")
# class SmartDevice(Device):
#     def __init__(self, device_id, connectivity):
#         super().__init__(device_id)
#         self.connectivity = connectivity

#     def connect(self):
#         print(f"{self.device_id} is connected via {self.connectivity}.")
# class SmartThermostat(SmartDevice):
#     def __init__(self, device_id, connectivity, temperature=20, mode="auto"):
#         super().__init__(device_id, connectivity)
#         self.temperature = temperature
#         self.mode = mode

#     def set_temperature(self, temp):
#         if temp < 10 or temp > 30:
#             print("Invalid temperature. Must be between 10 and 30.")
#             return
#         self.temperature = temp
#         print(f"Temperature set to {self.temperature}°C.")

#     def turn_on(self):
#         super().turn_on()
#         print(f"{self.device_id} is initializing with temperature {self.temperature}°C in {self.mode} mode.")
# # Example usage
# thermostat = SmartThermostat("Thermo1", "WiFi")
# thermostat.turn_on()
# thermostat.set_temperature(25)
# thermostat.set_temperature(35)  # Invalid temperature





# class Account:
#     def __init__(self, account_number, account_balance):
#         self.account_number = account_number
#         self.account_balance = account_balance
#         self.history = []

#     def deposit(self, amount):
#         self.account_balance = self.account_balance + amount
#         self.history.append(f"Deposited {amount}")

#     def withdraw(self, amount):
#         self.account_balance = self.account_balance - amount
#         self.history.append(f"Withdrawn {amount}")


# class SavingsAccount(Account):
#     def __init__(self, account_number, account_balance, interest_rate):
#         super().__init__(account_number, account_balance)
#         self.interest_rate = interest_rate

#     def add_interest(self):
#         calculated_interest = self.account_balance * self.interest_rate
#         self.deposit(calculated_interest)
#         self.history.append(f"Interest added: {calculated_interest}")


# class PremiumSavingsAccount(SavingsAccount):
#     def __init__(self, account_number, account_balance, interest_rate, reward_points):
#         super().__init__(account_number, account_balance, interest_rate)
#         self.reward_points = reward_points

#     def withdraw(self, amount):
#         if self.account_balance - amount < 50:
#             print("Cannot withdraw! Minimum balance of 50 must be maintained.")
#         else:
#             super().withdraw(amount)
#             print("Withdraw successful!")

#     def redeem_points(self):
#         self.deposit(self.reward_points)
#         self.reward_points = 0
#         self.history.append("Redeemed reward points")
#         print("Rewards redeemed successfully!")


# my_account = PremiumSavingsAccount(account_number=999, account_balance=100, interest_rate=0.05, reward_points=20)

# print(f"Starting Balance: {my_account.account_balance}")

# my_account.withdraw(20) 

# my_account.redeem_points()

# my_account.add_interest()

# print(f"Final Balance: {my_account.account_balance}")
# print("Transaction History:", my_account.history)




class Device:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = "off"

    def turn_on(self):
        self.status = "on"
        print(f"Device {self.device_id} is now ON.")

    def turn_off(self):
        self.status = "off"
        print(f"Device {self.device_id} is now OFF.")

class Thermostat(Device):
    def __init__(self, device_id, temperature):
        super().__init__(device_id)
        self.temperature = temperature

    def set_temperature(self, new_temp):
        if new_temp < 16 or new_temp > 30:
            print("Extreme! Temperature must be between 16 and 30.")
        else:
            self.temperature = new_temp
            print(f"Temperature safely set to {self.temperature}")

my_heater = Thermostat(device_id="LivingRoom_1", temperature=22)
my_heater.turn_on() 
my_heater.set_temperature(31)