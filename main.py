class Account:
  def __init__(self, pin, name, balance):
    self.pin = pin
    self.name = name
    self.balance = balance

accounts = {
    "001": {
        "name": "John",
        "balance": 25
    }
}

print(accounts["001"]["name"])

login = input("Do you have an account? y or n: ").lower()

if login == "y":
  pass
elif login == "n":
  user_name = input("What is your first name?: ").lower()
  pin_num = input("Please create a 4 digit pin: ")
  deposit = input("Would you like to submit an initial deposit? y or n").lower()
  if deposit == "y":
    balance = int(input("Please enter the amount you would like to deposit (only numbers no signs)"))
  else:
    balance = 0
  create_account(user_name, pin_num, balance)
else:
  print("Your input was invalid. Please try again.")
