import sqlite3

connect = sqlite3.connect("accounts.db")
print("Connected")

cursor = connect.cursor()


connect.close()