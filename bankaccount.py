class BankAccount:
  balance = 0
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return "%s's account. Balance: $%.2f" % (self.name, self.balance)

  def deposit(self, amount):
    if amount <= 0:
      print("Amount value is lower or equal 0")
      return
    else:
      print("Deposit is $%.2f" % (amount))
      self.balance += amount
      self.show_balance()

  def withdraw(self, amount):
    if amount > self.balance:
      print("Your balance is lower than %.2f" % (amount))
      return
    else:
      print("Amount is %.2f" % (amount))
      self.balance -= amount
      self.show_balance()

  def show_balance(self):
    print("Balance: $%.2f" % (self.balance))

# end class BankAccount


# ------------------------------------------------------------------
# test

my_account = BankAccount('Jane')
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)
