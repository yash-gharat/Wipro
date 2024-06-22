class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account_number, customer_name, initial_deposit=0):
        self.accounts[account_number] = {
            "customer_name": customer_name,
            "balance": initial_deposit
        }
        print(f"Account opened for {customer_name} with initial deposit of ${initial_deposit}.")

    def deposit(self, account_number, amount):
        self.accounts[account_number]['balance'] += amount
        print(
            f"${amount} deposited to account {account_number}. New balance is ${self.accounts[account_number]['balance']}.")

    def get_balance(self, account_number):
        return self.accounts[account_number]['balance']


# Example usage
bank = Bank()
bank.open_account("12345", "Sara", 1000)
bank.deposit("12345", 500)
print(f"Alice's balance: ${bank.get_balance('12345')}")
