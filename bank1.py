# customers
# accounts
# customer account should be update the status after withdraw and deposit
class bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def add_customer(self, customers_list):
        # extend instead of append since you're passing a list
        self.customers.extend(customers_list)
        print('Customers are added to the bank')

    def add_account(self, accounts_list):
        # extend instead of append since you're passing a list
        self.accounts.extend(accounts_list)
        print('Accounts are added to the bank')


class account:
    def __init__(self, account_id, account_name, balance, status="active"):
        self.account_id = account_id
        self.account_name = account_name
        self.balance = balance
        self.status = status
        self.customer = None

    def deposit(self, dep_amt):
        if dep_amt > 0 and self.status == "active":
            self.balance += dep_amt
            print(f"Deposited amount: {dep_amt}, Current balance: {self.balance}")
        else:
            print("Deposit failed. Account inactive or invalid amount.")

    def withdraw(self, wit_amt):
        if wit_amt > 0 and self.status == "active":
            if wit_amt <= self.balance:
                self.balance -= wit_amt
                print(f"Withdraw amount: {wit_amt}, Current balance: {self.balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Withdraw failed. Account inactive or invalid amount.")

    def setBalance(self):
        print(f'Current balance: {self.balance}')

    def getInfo(self):
        print(f'Name: {self.account_name}, '
              f'Account ID: {self.account_id}, '
              f'Balance: {self.balance}, '
              f'Status: {self.status}')


class customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def view_accounts(self):
        print(f"{self.name}'s Accounts:")
        for acc in self.accounts:
            acc.getInfo()


# --- Demo ---
b = bank()

c1 = customer(1, "John")
c2 = customer(2, "Stephen")
c3 = customer(3, "Rechen")

u1 = account(101, "Savings", 1000)
u2 = account(102, "Current", 30000)

customers = [c1, c2, c3]
accounts = [u1, u2]

# add list of customers/accounts
b.add_customer(customers)
b.add_account(accounts)

# link accounts manually to customers
c1.add_account(u1)
c2.add_account(u2)


u1.deposit(30000)
u1.withdraw(5000)


c1.view_accounts()
c2.view_accounts()
