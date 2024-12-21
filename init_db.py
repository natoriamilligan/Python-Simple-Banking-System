from db_connection import conn

sql_statements = [
    """CREATE TABLE IF NOT EXISTS accounts (
                account_id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                balance INTEGER NOT NULL,
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

    cursor = conn.cursor()

    cursor.execute(sql_statements)

    conn.commit()

    print("Tables created successfully")