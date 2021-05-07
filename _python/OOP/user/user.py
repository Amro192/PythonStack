import BankAccount
class User:	
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.5, balance=0)
        
    def make_deposit(self, amount):	
    	self.account.make_deposite(amount)
    
        

    def make_withdrawal(self, amount):
        if amount>=self.account.make_withdrawal(amount):
            print("There's NO money")
        else: 
            self.account.make_withdrawal(amount)

    def display_user_balance(self):
        print("user:",self.name,",balance:", self.account)

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        
amro=User("amro", "email@gmail.com")
