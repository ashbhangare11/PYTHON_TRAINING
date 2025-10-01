class BankAccount:
    def __init__(self, initial_balance=0):
        # Private variable - cannot be accessed directly from outside
        self.__balance = initial_balance
    
    # Private method - can only be used inside the class
    def __validate_amount(self, amount):
        if amount <= 0:
            return False
        return True
    
    # Public methods - can be called from outside
    def deposit(self, amount):
        if self.__validate_amount(amount):  # Using private method
            self.__balance += amount
            return self.__balance
        return "Error: Amount must be positive"
    
    def withdraw(self, amount):
        if not self.__validate_amount(amount):
            return "Error: Amount must be positive"
        
        if amount > self.__balance:
            return "Error: Insufficient funds"
        
        self.__balance -= amount
        return self.__balance
    
    def check_balance(self):
        return self.__balance


# Using the BankAccount
account = BankAccount(100)  # Start with $100

print("Your account balance is: ", account.check_balance())                  # ✓ Works - public method
print("Your account balance after deposit is: ", account.deposit(50))        # ✓ Works - uses private method internally
print("Your account balance after withdrawl is: ",account.withdraw(30))      # ✓ Works - uses private method internally
print(account.withdraw(200))   						     # ✓ Works - shows error properly
print(account.deposit(-10))   						     # ✓ Works - shows error properly
print("Your final account balance is: ",account.check_balance())             # Final balance

# These will cause ERRORS if uncommented:
# print(account.__balance)       # ❌ Error - private variable
# account.__validate_amount(50)  # ❌ Error - private method