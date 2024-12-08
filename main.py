import json

try:
  with open("accounts.json", "r") as file:
      accounts = json.load(file)
      print(accounts)
except:
  with open("accounts.json", "x") as file:
      json.dump({}, file)

def create_account(username, pin, bal):
  accounts[username] = {"username": username, "pin": pin, "balance": bal}
  with open("accounts.json", "w") as file:
    json.dump(accounts, file)

def access_account():
  action = input("Would you like to make a deposit or a withdrawl? d or w").lower()

def login():
  login = input("Do you have an account? y or n: ").lower()
  while True:
    if login == "y":
      user_valid = input("What is your username? :").lower()
      if user_valid not in accounts:
        print("User invalid. Please try again")
        continue
      else: 
        pin_valid = input("What is your pin? :")

        if user_valid in accounts and pin_valid == accounts[user_valid]["pin"]:
          print(f"You've successfully logged in! Your balance is: ${accounts[user_valid]['balance']}.")
        access_account()
    elif login == "n":
      username = input("Please create a username: ").lower()
      if username in accounts:
        username = input("That username has been taken. Please create a username: ").lower()
      pin_num = input("Please create a 4 digit pin: ")

      deposit = input("Would you like to submit an initial deposit? y or n").lower()

      if deposit == "y":
        balance = int(input("Please enter the amount you would like to deposit (only numbers no signs)"))
      else:
        balance = 0

      create_account(username, pin_num, balance)
      print(accounts)
      break
    else:
      print("Your input was invalid. Please try again.")

login()
