class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        
    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))
    
class Checking(Account):
    """This class generates checking account objects"""
    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

jacks_checking = Checking('account/jack.txt', 13)
jacks_checking.transfer(11)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)

johns_checking = Checking('account/john.txt', 13)
johns_checking.transfer(11)
print(johns_checking.balance)
johns_checking.commit()
print(johns_checking.type)

print(johns_checking.__doc__)
