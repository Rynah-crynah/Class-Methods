from optparse import AmbiguousOptionError
import re


class Account:
    def __init__( self,fullName,accountNumber,branch):
        self.fullName=fullName
        self.accountNumber=accountNumber
        self.branch=branch
        self.accountbalance=0
        self.deposits=[]
        self.withdrawals=[]
       
        

    # def deposit(self,amount):
    #     self.amount=amount
    #     return f'{self.fullName} your new balance is {self.accountBalance + self.amount}'
       
    def deposit(self, amount):
        if amount<=0:
           return f"Deposit amount must be greater than zero "    
        else:
            self.accountbalance+=amount
            self.deposits.append(amount)
            return f"Hello {self.fullName} you have deposited {amount} from {self.branch}. Your new balance is {self.accountbalance}"
   
    def withdraw(self, amount):
        if amount>self.accountbalance:
           return f"Hello {self.fullName} you have deposited {self.accountbalance}, you can't withdraw your balance is insuficient"
        elif amount<=0:
            return f"Amount must be greater than zero"
        else:
            self.accountbalance-=amount
            self.withdrawals.append(amount)
            self.transaction_cost=100
            self.accountbalance-=amount+ self.transaction_cost

            return f"Hello {self.fullName} you have withdrawn {amount}  from {self.branch} and your new balance is {self.accountbalance}"

    def deposit_stmt(self):
        for deposit in self.deposits:
            print(f"Hello {self.fullName} you have withdrawn KES{self.withdrawals} from {self.branch}")

    def withdrawals_stmt(self):
        for withdraw in self.withdrawals:
            print(f"You have withdrawn KES {withdraw}")

    def withdrawals(self,amount):
        if amount >0:
            self.accountbalance-=amount+100
            return f"Hello {self.fullName}, you have withdrawn {amount} and your new balance is {self.accountbalance}"
        elif amount <0:
            return f"Withdraw amount must be greater than zero"
        elif amount== self.accountbalance:
            return f"Insufficient" 
        else:
            return f"Insufficients funds"

    def current_bal(self):
        return f"The current balance is KSH {self.accountbalance}"   
   
    



 