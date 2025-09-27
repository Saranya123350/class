# customers
# accounts
# customer account should be update the status after withdraw and deposit
class bank:
    def __init__(self):
        self.customers=[]
        self.accounts=[]
    def add_customer(self, customer):
        self.customers.append(customer)
        print("Customer added to the bank")
    def add_account(self, account, customer):
        self.accounts.append(account)
        print("accounts added to the bank")
        
 
class account:
    def __init__(self,account_id, account_name,balance, status="active"):
        self.account_id = account_id 
        self.account_name = account_name 
        self.balance = balance
        self.status = status 
        self.customer=None
    def deposit(self,balance, dep_amt):
        if (dep_amt>0 and self.status == "active"):
                balance+=dep_amt 
                self.balance=balance
                print(f"deposted amount:{dep_amt} , current_balance: {balance}")
        else:
            print("Withdraw failed. Account inactive or invalid amount.")
        
    def withdraw(self,balance, wit_amt):
        if (wit_amt>0 and self.status == "active"):
            balance-=wit_amt
            self.balance=balance
            print(f"withdraw_amount:{wit_amt} , current_balance: {balance}")
        else:
            print("Withdraw failed. Account inactive or invalid amount.")
    def setBalance(self):
        print(f'current_balance: {self.balance}')
    def getInfo(self):
        print(f'Name: {self.account_name}, account ID: {self.account_id} , balance: {self.balance} , deposit: {self.deposit}, withdraw amount:{self.withdraw}')
    
class customer:
    def __init__(self,id,name):
        self.id=id 
        self.name=name 
        self.accounts = []   

    def add_account(self, account):
        self.accounts.append(account)
    def view_accounts(self):
        print(f"{self.name}'s Accounts:")
        for acc in self.accounts:
            acc.getInfo()
    
b=bank()

c1 = customer(1, "John")
c2 = customer(2, "Stephen")
c3 = customer(3, "Rechen")
u1 = account(101, "Savings", 1000)
u2 = account(102, "Current", 30000)
customers=[c1,c2,c3]
accounts=[u1,u2]
b.add_customer(customers)
b.add_account(accounts)



u1.deposit(500000,30000)
u1.withdraw(200000,30000)


c1.view_accounts()


