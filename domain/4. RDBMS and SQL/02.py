# 2. Write a program wo create a class representing
# a bank include methods for managing customer accounts
# and do transactions like open account or deposit

from db_config import MySQLService

my_sql_service = MySQLService()
connection = my_sql_service.get_mysql_connection(database="bank")

def create_account_table(connection):
    cursor = connection.cursor()
    query = '''CREATE TABLE IF NOT EXISTS ACCOUNTS (
                account_number INT AUTO_INCREMENT PRIMARY KEY,
                customer_name VARCHAR(255) NOT NULL,
                balance INT NOT NULL
    )'''
    cursor.execute(query)
    connection.commit()
    cursor.close()

def open_account(connection, customer_name, balance):
    cursor = connection.cursor()
    query = 'INSERT INTO ACCOUNTS(customer_name, balance) VALUES (%s, %s)'
    cursor.execute(query, (customer_name, balance))
    connection.commit()
    cursor.close()

def deposit(connection, account_number, amount):
    cursor = connection.cursor()
    query = 'UPDATE ACCOUNTS SET balance = balance + %s WHERE account_number = %s'
    cursor.execute(query, (amount, account_number))
    connection.commit()
    cursor.close()

def get_balance(connection, account_number):
    cursor = connection.cursor()
    query = 'SELECT balance FROM ACCOUNTS WHERE account_number = %s'
    cursor.execute(query, (account_number,))
    balance = cursor.fetchone()[0]  # Fetch the balance value from the result tuple
    cursor.close()
    return balance

def input_open_account(connection):
    customer_name = input("Enter customer name: ")
    balance = int(input("Enter initial balance: "))
    open_account(connection, customer_name, balance)
    print(f"Account opened for {customer_name} with balance ${balance}")

def input_deposit(connection):
    account_number = int(input("Enter account number: "))
    amount = int(input("Enter deposit amount: "))
    deposit(connection, account_number, amount)
    print(f"Deposited ${amount} into account {account_number}")

def input_check_balance(connection):
    account_number = int(input("Enter account number: "))
    balance = get_balance(connection, account_number)
    print(f"Balance of account {account_number}: ${balance}")

if __name__ == "__main__":
    create_account_table(connection)

    while True:
        print("\n1. Open Account")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            input_open_account(connection)
        elif choice == '2':
            input_deposit(connection)
        elif choice == '3':
            input_check_balance(connection)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
