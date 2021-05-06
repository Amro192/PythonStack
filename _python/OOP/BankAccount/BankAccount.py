class BankAccount:
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate=0.5
        self.balance=balance
       
		
    def deposit(self, amount):
        self.balance+= amount

    def withdraw(self, amount):
        if amount> self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        else:  
            self.balance-= amount
		
    def display_account_info(self):
        print("Balance:$",self.balance)

    def yield_interest(self):
        if self.balance>0:
            self.balance = self.balance * self.int_rate

FirstAC = BankAccount()
FirstAC.balance=500
FirstAC.deposit(20)
FirstAC.deposit(20)
FirstAC.deposit(20)
FirstAC.withdraw(30)
FirstAC.yield_interest()
FirstAC.display_account_info()


SecondAc = BankAccount()
SecondAc.deposit(20)
SecondAc.deposit(20)
SecondAc.withdraw(30)
SecondAc.withdraw(30)
SecondAc.withdraw(30)
SecondAc.withdraw(30)
FirstAC.yield_interest()
FirstAC.display_account_info()