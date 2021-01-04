#1.) class creation: features shared by all users:
class Account:
	def __init__(self,acct_nbr,opening_deposit):
		self.acct_nbr=acct_nbr
		self.balance=opening_deposit

	def __str__(self):
		return f'Rs.{self.balance:.2f}'

	def deposit(self,dep_amt):
		self.balance+=dep_amt

	def withdraw(self,wd_amt):
		if self.balance>=wd_amt:
			self.balance-=wd_amt
		else:
			return 'Funds Unavailable'

#2.) class checking, to check traits
class Checking(Account):
	def __init__(self,acct_nbr,opening_deposit):
		super().__init__(acct_nbr,opening_deposit)

	def __str__(self):
		return f'Checking Account #{self.acct_nbr}\n Balance: {Account.__str__(self)}'

x=Checking(99885624,8968211.226)
print(x)
