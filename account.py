class Account:
    def __init__( self,fullName,accountNumber,branch,accountBalance):
        self.fullName=fullName
        self.accountNumber=accountNumber
        self.branch=branch
        self.accountBalance=accountBalance
        

    def deposit(self,amount):
        self.amount=amount
        return f'{self.fullName} your new balance is {self.accountBalance + self.amount}'

    def withdraw(self,withdrawal):
        self.withdrawal=withdrawal
        return f'{self.fullName} your new balance is {self.accountBalance - self.withdrawal}'
