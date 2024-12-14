import json

try:
  with open("accounts.json", "r") as file:
      accounts = json.load(file)
except:
  with open("accounts.json", "w") as file:
      json.dump({}, file)

def create_account():
  username = input("Please create a username: ").lower()
  if username in accounts:
    username = input("That username has been taken. Please create a username: ").lower()
  else:
    pin_num = input("Please create a 4 digit pin: ")
    deposit = input("Would you like to submit an initial deposit? y or n").lower()

  if deposit == "y":
     balance = float(input("Please enter the amount you would like to deposit (only numbers no signs)"))
     history = {"type": "deposit", "amount": balance }
  elif deposit == "n":
    balance = 0
  else:
    print("Input was invalid. Please start over")
    create_account()
  accounts[username] = {"username": username, "pin": pin_num, "balance": balance, "history": [history]}
  with open("accounts.json", "w") as file:
    json.dump(accounts, file)

def edit_name(user):
    new_name = input("Please type in your new username: ").lower()
    accounts[new_name] = accounts[user]
    accounts[new_name]["username"] = new_name
    del accounts[user]
    with open("accounts.json", "w") as file:
      json.dump(accounts, file)
    print(f"You have successfully changed your username to {new_name}")
    return new_name

def edit_pin(user):
    new_pin = input("Please type in your new pin: ").lower()
    accounts[user]["pin"] = new_pin
    with open("accounts.json", "w") as file:
      json.dump(accounts, file)
    print(f"You have successfully changed your pin.")
    print(accounts[user])
    return new_pin

def access_account(user):
    while True:
      action = input("Would you like to make a deposit, withdrawal, transfer, view transaction history, or edit your profile? d, w, t, v, or e").lower()
      if action == "d":
        deposit_amt = float(input("How much would you like to deposit?"))
        new_balance = float(accounts[user]["balance"] + deposit_amt)
        new_dep = {"type": "deposit", "amount": f"${deposit_amt:.2f}"}
        accounts[user]["balance"] = new_balance
        accounts[user]["history"].append(new_dep)

        with open("accounts.json", "w") as file:
          json.dump(accounts, file)

        print(f"Your new balance is: ${accounts[user]['balance']:.2f}.")
      elif action == "w":
        withdrawl_amt = float(input("How much would you like to withdrawl?"))
        new_balance = float(accounts[user]["balance"] - withdrawl_amt)
        if new_balance < 0:
          print("You do not have enough funds to withdrawl. Please try again")
          continue
        else:
          new_withdrawl = {"type": "withdrawal", "amount": f"${withdrawl_amt:.2f}"}
          accounts[user]["balance"] = new_balance
          accounts[user]["history"].append(new_withdrawl)

          with open("accounts.json", "w") as file:
            json.dump(accounts, file)

          print(f"Your new balance is: ${accounts[user]['balance']:.2f}.")
      elif action == "t":
        while True:
          recipient = input("Type in the username of the account you would like to tranfer money to: ").lower()
          if recipient in accounts:
            print(f"Your balance is: ${accounts[user]['balance']:.2f}.")
            amt_transfer = float(input("How much money would you like to transfer?"))
            accounts[recipient]["balance"] = accounts[recipient]["balance"] + amt_transfer
            
            accounts[user]["balance"] = accounts[user]["balance"] - amt_transfer
            new_trans = {"type": "transfer", "amount": amt_transfer, "recipient": recipient}
            accounts[user]["history"].append(new_trans)

            with open("accounts.json", "w") as file:
              json.dump(accounts, file)
            
            print(f"You have successfully transferred ${amt_transfer:.2f} to {recipient}.")
            break
          else:
            print("That username is invalid, please try again.")
            continue

      elif action == "v":
        print(accounts[user]["history"])
      elif action == "e":
        while True:
          edit_option = input("Would you like to change your username or pin? u or p").lower()

          if edit_option == "u":
            user = edit_name(user)
            break
          elif edit_option == "p":
            accounts[user]["pin"] = edit_pin(user)
            break
          else:
            print("You entered an invalid input. Please try again")
            continue
      else:
        print("You entered an invalid input.")
        continue

      user_active = input("Would you like to logout or do another action? Type action or logout.").lower()
      if user_active == "action":
        continue
      elif user_active == "logout":
        print("You have been successfully logged out.")
        break
      else:
        print("Invalid input. You have been logged out.")
        break

def login():
  login = input("Do you have an account? y or n: ").lower()
  while True:
    if login == "y":
      user_valid = input("What is your username? :").lower()
      if user_valid not in accounts:
        try_again = input("User invalid. Would you like to create account or retype your username? Type create or retype:").lower()
        if try_again == "create":
           create_account()
           print(f"You've successfully created your account! Your new balance is: ${accounts[user_valid]['balance']:.2f}.")
           break
        elif try_again == "retype":
          continue
        else:
          try_again = input("Invalid input. Would you like to create account or retype your username? Type create or retype:").lower()
      else:
        pin_valid = input("What is your pin? :")

        if user_valid in accounts and pin_valid == accounts[user_valid]["pin"]:
          print(f"You've successfully logged in! Your balance is: ${accounts[user_valid]['balance']:.2f}.")
          access_account(user_valid)
          break
        else:
          print("Invalid input. Please try again")
          continue
    elif login == "n":
      print("Let's get you an account created!")
      create_account()
      break
    else:
      print("Your input was invalid. Please try again later.")
      break

login()