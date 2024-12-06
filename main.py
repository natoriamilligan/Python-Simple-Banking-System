import json

with open("accounts.json", "r") as file:
    accounts = json.load(file)
    print(accounts)

def create_account(name, pin, bal):
  accounts[pin] = {"name": name, "balance": bal}
  with open("accounts.json", "w") as file:
    json.dump(accounts, file)

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
  print(accounts)
else:
  print("Your input was invalid. Please try again.")
