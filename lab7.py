import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def select_all_accounts(conn):
    sql = 'SELECT a.AccountId, a.Balance, c.Name FROM Accounts a JOIN Clients c ON a.ClientId = c.ClientId'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_all_clients(conn):
    sql = 'SELECT c.ClientID, c.Name, c.Email FROM Clients c'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_all_transactions(conn):
    sql = 'SELECT t.TransactionId, t.Amount, t.Date, c.Name FROM Transactions t JOIN Accounts a ON t.AccountId = a.AccountId JOIN Clients c ON a.ClientId = c.ClientId'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def create_client(conn, name, email):
    sql = ''' INSERT INTO Clients(Name, Email)
              VALUES(?, ?) '''
    values = (name, email)
    cur = conn.cursor()
    cur.execute(sql, values)

def create_account(conn, balance, clientid):
    sql = ''' INSERT INTO Accounts(Balance, ClientId)
              VALUES(?, ?) '''
    values = (balance, clientid)
    cur = conn.cursor()
    cur.execute(sql, values)

def create_transaction(conn, amount, date, accountid):
    sql = ''' INSERT INTO Transactions(Amount, Date, AccountId)
              VALUES(?, ?, ?) '''
    values = (amount, date, accountid)
    cur = conn.cursor()
    cur.execute(sql, values)

def update_client(conn, name, email, clientid):
    sql = ''' UPDATE Clients
              SET Name = ?, Email = ?
              WHERE ClientId = ?'''
    values = (name, email, clientid)
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()

def update_account(conn, balance, accountid):
    sql = ''' UPDATE Accounts
              SET Balance = ?
              WHERE AccountId = ?'''
    values = (balance, accountid)
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()

def update_transaction(conn, amount, date, accountid):
    sql = ''' UPDATE Transactions
              SET Amount = ?, Date = ?
              WHERE AccountId = ?'''
    values = (amount, date, accountid)
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()

def delete_transaction(conn, transactionid):
    sql = '''DELETE FROM Transactions
             WHERE TransactionId = ?'''
    values = (transactionid,)
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()

def main():
    database = r"db.db" 
    conn = create_connection(database)
    
    with conn:
        delete_transaction(conn, 3)
        
 
if __name__ == '__main__':
    main()