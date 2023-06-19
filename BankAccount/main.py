class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def recieve(self, amount):
        if amount > self.balance:
            return ValueError("Insufficient Amount of Money")
        self.balance -= amount
        
    
    def get_balance(self):
        return self.balance

def main():
    bank_account = BankAccount( "126352", "John Steve", 3400)

    bank_account.deposit(24)
    bank_account.recieve(400)

    print(bank_account.get_balance())

if __name__ == "__main__":
    main()