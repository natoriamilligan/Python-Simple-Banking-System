from db_connection import conn, sqlite3

sql_statements = [
    """CREATE TABLE IF NOT EXISTS accounts (
                account_id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                balance INTEGER NOT NULL
        );""",

    """CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY,
            trans_type TEXT NOT NULL,
            amount INTEGER NOT NULL,
            account_id INTEGER NOT NULL,
            FOREIGN KEY (account_id)
            REFERENCES accounts (account_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        );"""
]

def initialize_database():
    print("Connection running")

    try:
        cursor = conn.cursor()
        print("cursor created")
        for statement in sql_statements:
            cursor.execute(statement)

        conn.commit()

        print("Tables created successfully")
    except sqlite3.OperationalError as e:
        print("Failed to create tables:", e)

initialize_database()
