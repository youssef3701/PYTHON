# In this project, you are required to first let user choose either to sign
# in or create a new account (Max of 50 accounts are available).
# ▪ Signing in: you must check if the account number and password are
# correct if account number or password are incorrect give the user
# another chance.
# ▪ Creating a new account: by taking the username, setting a unique
# account number of 4 numbers, and let the user choose his password
# after that the user should deposit a minimum of 5000 dollars.
# ▪ Then there are several options:
# ▪ Either to Check balance, deposit, withdraw, change password or exit
# the user should choose several options until he chooses exit then the
# system stops
import  random
import string
import random
import string

import random
import string

class BankAccountSystem:
    def __init__(self, account_number, balance, password, username):
        self.Max_size = 50
        self.accounts = []
        self._account_number = account_number
        self._balance = balance
        self._password = password
        self._username = username

    def create_account(self, username, balance, password, account_number):
        if self.get_account_by_account_number(account_number) or self.get_account_by_user_name(username):
            print("account exists")
            return False
        return True

    def get_account_by_account_number(self, account_number):
        for account in self.accounts:
            if account["account_number"] == account_number:
                return account
        return None

    def get_account_by_user_name(self, user_name):
        for account in self.accounts:
            if account["username"] == user_name:
                return account
        return None

    def generate_password(self, length, uppercase=True, lowercase=True, special_chars=True, digits=True):
        characters = ''
        if lowercase:
            characters += string.ascii_lowercase
        if uppercase:
            characters += string.ascii_uppercase
        if digits:
            characters += string.digits
        if special_chars:
            characters += string.punctuation
        if not characters:
            return "Error: No character set selected."
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def set_account_number(self, account_number):
        self._account_number = account_number

    def get_account_number(self):
        return self._account_number

    def set_balance(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            print("NOT VALID")
        else:
            self._balance -= amount

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("NOT VALID")

def main():
    bank_account_system = BankAccountSystem(0, 0, '', '')



    choose = int(input("Hello sir! What would you like to do?\n"
                       "1- Create a new account\n"
                       "2- Sign in\n"
                       "3- Exit\nChoose between (1, 2, 3): "))

    if choose == 1:
        user_name = str(input("ENTER A VALID USER-NAME PLEASE: "))
        unique_account_number = random.randint(1000, 9999)
        print(f"Your account number is {unique_account_number}")
        # print("Welcome to the Password Generator!")
        length = int(input("Enter the desired password length: "))
        use_lowercase = input("Use lowercase letters? (y/n): ").lower() == 'y'
        use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Use digits? (y/n): ").lower() == 'y'
        use_special_chars = input("Use special characters? (y/n): ").lower() == 'y'
        password = bank_account_system.generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
        print("Generated password your password is:", password)
        print("NOW YOU SHOULD MAKE A DEPOSIT INTO YOUR ACCOUNT WITH A MINIMUM AMOUNT 5000 DOLLAR")
        amount = int(input('ENTER THE AMOUNT OF MONEY: '))
        if amount < 5000:
            print("NOT VALID")
        else:
            bank_account_system.deposit(amount)
            print(f"Your balance is {bank_account_system.get_balance()}")

    while choose == 1:

        options = int(input("What do you want to do?:\n"
                            "1- check balance\n"
                            "2- deposit\n"
                            "3- withdraw\n"
                            "4- change password\n"
                            "5- exit\nChoose between (1, 2, 3, 4, 5): "))

        if options == 1:

            print(f"Your balance is {bank_account_system.get_balance()}")

        elif options == 2:
            amount = int(input("Enter the amount of money to deposit: "))
            if amount < 5000:
                print("NOT VALID")
            else:
                bank_account_system.deposit(amount)
                print(f"Your new balance is {bank_account_system.get_balance()}")

        elif options == 3:
            amount = int(input("Enter the amount of money to withdraw: "))
            bank_account_system.withdraw(amount)
            print(f"Your new balance is {bank_account_system.get_balance()}")

        elif options == 4:
            length = int(input("Enter the desired password length: "))
            use_lowercase = input("Use lowercase letters? (y/n): ").lower() == 'y'
            use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
            use_digits = input("Use digits? (y/n): ").lower() == 'y'
            use_special_chars = input("Use special characters? (y/n): ").lower() == 'y'
            password = bank_account_system.generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
            print(f"Your new password is: {password}")

        elif options == 5:
            print("Exiting...")
            break
        else:
            print("Not a valid option. Please choose again.")

    while choose == 2 :
        user_name = str(input("Enter your user-name: "))
        if bank_account_system.get_account_by_user_name(user_name):
            print(f"your user name is correct ")
        else:
            print("this user name is false ")

        account_number = int(input("Enter your account number: "))
        if bank_account_system.get_account_by_account_number(account_number):
            print("your account number is correct")
        else:
            print("your account number is false: ")

    while choose == 3 :
        print("exit")
        break

if __name__ == "__main__":
    main()


