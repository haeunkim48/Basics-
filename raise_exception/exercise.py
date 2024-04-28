class AdultException (Exception):
    pass

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    def get_minor_age(self):
        if int(self.age) >= 18: 
            raise AdultException
        else: 
            return self.age
    
    def display_person (self):
        try:
            print(f"age -> {self.get_minor_age()}")
        except AdultException:
            print("Person is an adult")
        finally:
            print(f"name -> {self.name}")

# no exception 
Person ('Grace', 17).display_person()

# Create a custom exception called InsufficientFundsException.

# Design a class BankAccount with attributes account_number, balance, and owner_name.

# Implement a method withdraw(amount) in the BankAccount class. This method should check if the account balance is sufficient to cover the withdrawal amount. If the balance is sufficient, it should deduct the amount from the balance and return the new balance. If the balance is insufficient, it should raise the InsufficientFundsException with an appropriate error message.

# Implement a method display_account_info() in the BankAccount class. This method should print the account number, owner's name, and current balance.

class InsufficientFundsExcpetion(Exception):
    pass 

class BankAccount: 
    def __init__ (self, account_number, balance, owner_name)
        self.account_number = account_number
        self.balance = balance 
        self.owner_name = owner_name

    def withdraw(self, amount):
        if amount > self.balance
            raise InsufficientFundsExcpetion ('Insufficient funds to withdraw')
        else: 
            self.balance -= amount 
            return self.balance


    def display_amount_info(self):
        print("Account Number:", self.account_number)
        print("Owner's Name:", self.owner_name)
        print("Current Balance:", self.balance)
            

    
