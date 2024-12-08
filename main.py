import json

try:
  with open("accounts.json", "r") as file:
      accounts = json.load(file)
      print(accounts)
except:
  with open("accounts.json", "w") as file:
      json.dump({}, file)

def create_account(user_acct):
  username = input("Please create a username: ").lower()
  if username in user_acct:
    username = input("That username has been taken. Please create a username: ").lower()
  pin_num = input("Please create a 4 digit pin: ")

  deposit = input("Would you like to submit an initial deposit? y or n").lower()

  if deposit == "y":
        balance = int(input("Please enter the amount you would like to deposit (only numbers no signs)"))
  else:
        balance = 0
  user_acct[username] = {"username": username, "pin": pin_num, "balance": balance}
  with open("accounts.json", "w") as file:
    json.dump(user_acct, file)

def access_account():
  action = input("Would you like to make a deposit or a withdrawl? d or w").lower()

def login(acct):
  login = input("Do you have an account? y or n: ").lower()
  while True:
    if login == "y":
      user_valid = input("What is your username? :").lower()
      if user_valid not in acct:
        try_again = input("User invalid. Would you like to create account or retype your username? Type create or retype:").lower()
        if try_again == "create":
           create_account(acct)
           print("You've successfully create your account!")
           break
        elif try_again == "retype":
          continue
      else: 
        pin_valid = input("What is your pin? :")

        if user_valid in acct and pin_valid == acct[user_valid]["pin"]:
          print(f"You've successfully logged in! Your balance is: ${accounts[user_valid]['balance']}.")
        access_account()
    elif login == "n":
      create_account(acct)
      print(acct)
      break
    else:
      print("Your input was invalid. Please try again.")

login(accounts)
