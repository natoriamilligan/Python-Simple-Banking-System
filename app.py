from db_connection import conn, sqlite3

def get_accounts():
    cursor = conn.cursor()
    cursor.execute("SELECT * from accounts")
    rows = cursor.fetchall()
    conn.close
    for row in rows:
        print(row)

get_accounts()