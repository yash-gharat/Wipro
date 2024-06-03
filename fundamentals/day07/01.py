#Encapsulation -  Encapsulation is like a safe with a lock.
# It keeps your data protected and only allows access through specific methods,
# ensuring that it's handled safely and securely.

class Customer:
    def __init__(self,id,name,age,wallet_balance) -> None:
        self.__id = id #private attribute
        self.name = name
        self.age = age
        self.wallet_balance = wallet_balance

    def update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount

    def show_balance(self):
        return self.wallet_balance