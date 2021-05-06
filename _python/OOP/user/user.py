class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
        

    def make_withdrawal(self, amount):
        if amount>=self.account_balance:
            print("There's NO money")
        else: 
            self.account_balance-= amount

    def display_user_balance(self):
        print("user:",self.name,",balance:", self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance-= amount
        other_user.account_balance += amount

Amro = User("amro","aaa@gmail.com")
Amro.account_balance=500
Amro.make_deposit(10)
Amro.make_deposit(10)
Amro.make_deposit(10)
Amro.make_withdrawal(30)
Amro.display_user_balance()

Tasneem = User("Tasneem", "email@sss")
Tasneem.account_balance=500
Tasneem.make_deposit(20)
Tasneem.make_deposit(20)
Tasneem.make_withdrawal(30)
Tasneem.make_withdrawal(30)
Tasneem.display_user_balance()

Diaa = User("Diaa","diaa@hhh")
Diaa.account_balance=350
Amro.transfer_money(Diaa, 50)
Diaa.display_user_balance()
