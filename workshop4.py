class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name
        print("Your name has been changed to", name)

    def change_pin(self, pin):
        self.pin = pin
        print("Your pin has been changed to", pin)

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", password)

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has a balance of: $", self.balance )

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient funds")

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, user, amount):
        print("You are transferring ${} to {}.".format(amount, user))
        pin_confirm = int(input("Authorization Required. Please enter your pin."))
        if pin_confirm == self.pin:
            self.balance -= amount
            user.balance += amount
            print("${} has been transferred to {}.".format(amount, user))
            return True
        else:
            print("Incorrent pin. Transaction cancelled.")
            return False

    def request_money(self, user, amount):
        print("You are requesting ${} from {}.".format(amount, user))
        user_pin = int(input("Authorization required. Please enter {}'s password.".format(user)))
        self_password = input("Please enter your password to finish authorization.")
        if user_pin == user.pin and self_password == self.password:
            user.balance -= amount
            self.balance += amount
            print("{} has been transferred to your account from {}'s account".format(amount, user.name))
            return True
        elif user_pin != user.pin:
            print("Incorrect pin for {}. Transaction cancelled".format(user.name))
            return False
        elif self_password != self.password:
            print("Incorrect password for {}.".format(self.name))
            return False
        



""" Driver Code for Task Five """
"""
bankuser1 = BankUser("Bob", 1234, "password")
bankuser2 = BankUser("Alice", 5678, "alicepassword")
bankuser2.deposit(5000)
bankuser2.show_balance()
bankuser1.show_balance()


transferred = bankuser2.transfer_money(bankuser1, 500)
bankuser2.show_balance()
bankuser1.show_balance()

​
if transferred:
   bankuser2.request_money(bankuser1, 250)
   bankuser2.show_balance()
   bankuser1.show_balance()
"""

"""Driver Code for Task 4"""

##  user = BankUser("Jay", 1234, "pwrd")

"""user.show_balance()
user.deposit(160)
user.show_balance()
user.withdraw(180)
user.show_balance()"""


"""Driver Test for Task 3"""
"""user = BankUser("Jay", 1234, "pwrd")

print(user.name)
print(user.pin)
print(user.password)
print(user.balance)"""

""" Driver Test for Task 2 """

"""user2 = User("Jan", 1234, "password")

user2.change_name("Janet")
user2.change_pin(4587)
user2.change_password("newpass")

print(user2.name)
print(user2.pin)
print(user2.password)"""
    



""" Driver Code for Task 1"""

"""user1 = User("Bob", 1234, "password")

print(user1.name)
print(user1.pin)
print(user1.password)"""
