# from optparse import AmbiguousOptionError
# import re


# class Account:
#     def __init__( self,fullName,accountNumber,branch):
#         self.fullName=fullName
#         self.accountNumber=accountNumber
#         self.branch=branch
#         self.accountbalance=0
#         self.deposits=[]
#         self.withdrawals=[]
       
        

#     # def deposit(self,amount):
#     #     self.amount=amount
#     #     return f'{self.fullName} your new balance is {self.accountBalance + self.amount}'
       
#     def deposit(self, amount):
#         if amount<=0:
#            return f"Deposit amount must be greater than zero "    
#         else:
#             self.accountbalance+=amount
#             self.deposits.append(amount)
#             return f"Hello {self.fullName} you have deposited {amount} from {self.branch}. Your new balance is {self.accountbalance}"
   
#     def withdraw(self, amount):
#         if amount>self.accountbalance:
#            return f"Hello {self.fullName} you have deposited {self.accountbalance}, you can't withdraw your balance is insuficient"
#         elif amount<=0:
#             return f"Amount must be greater than zero"
#         else:
#             self.accountbalance-=amount
#             self.withdrawals.append(amount)
#             self.transaction_cost=100
#             self.accountbalance-=amount+ self.transaction_cost

#             return f"Hello {self.fullName} you have withdrawn {amount}  from {self.branch} and your new balance is {self.accountbalance}"

#     def deposit_stmt(self):
#         for deposit in self.deposits:
#             print(f"Hello {self.fullName} you have withdrawn KES{self.withdrawals} from {self.branch}")

#     def withdrawals_stmt(self):
#         for withdraw in self.withdrawals:
#             print(f"You have withdrawn KES {withdraw}")

#     def withdrawals(self,amount):
#         if amount + self.trasactional_cost >self.accountbalance:
#             print()



#         # if amount >0:
#         #     self.accountbalance-=amount+100
#         #     return f"Hello {self.fullName}, you have withdrawn {amount} and your new balance is {self.accountbalance}"
#         # elif amount <0:
#         #     return f"Withdraw amount must be greater than zero"
#         # elif amount== self.accountbalance:
#         #     return f"Insufficient" 
#         # else:
#         #     return f"Insufficients funds"

#     def current_bal(self):
#         return f"The current balance is KSH {self.accountbalance}"   
   
    
from datetime import datetime
class Account:
    def __init__(self,fullName,accountNumber):
        self.fullName = fullName
        self.accountNumber = accountNumber
        self.accountBalance = 0
        self.transactionFee = 100
        self.loan=0
        self.deposits=[]
        self.withdrawals = []
        self.statement = []



    def  deposit(self,amount):
        if amount <=0:
             print(f"Deposit must be a positive amount")
        else:
            self.accountBalance+=amount
            now= datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"You have deposited"
            }
            self.deposits.append(amount)
            self.statement.append(transaction)
            print(f"Hello {self.fullName}, your new balance is {self.accountBalance} and your deposits are {self.deposits}and your statement is {self.statement}" )
    def withdrawal(self,amount):

        if amount+self.transactionFee > self.accountBalance:
            print(f"Hello {self.fullName}, your balance is {self.accountBalance} you can't withdraw {amount}")
        elif amount <=0:
            print(f"Withdrawal amount must be greater than 0")
        else:
            self.accountBalance-=amount+self.transactionFee
            now= datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"You have withdrawn "
            }
            self.withdrawals.append(amount)
            self.statement.append(transaction)
            print(f"Hello {self.fullName}, your new balance is {self.accountBalance} and the withdrawals are {self.statement}")
    def deposit_statements(self):
         for deposit in self.statement:
             print(deposit)

    def withdrawals_statement(self):
        for withdrawal in self.statement:
            print(withdrawal)

    def current_balance(self):
        print(f"{self.accountBalance}")



    def full_Statement(self):
        for transaction in self.statement:
            amount = transaction["amount"]
            Narration= transaction["Narration"]
            time= transaction["time"]
            date= time.strftime("%x/%X")
            print(f"{date}:   {Narration}   {amount}")

    def borrow(self,amount):
        item = len(self.deposits)
        item_s = sum(self.deposits)
        limit = item_s*(1/3)
        amount+=(amount)*0.03

        if amount<=100:
            return "Sorry we can't give you this loan, your loan must be more than 100 "
        elif self.loan>0:
            return f"Dear customer you still have a loan of {self.loan}"
        elif item<10:
            return f"Your deposits must be atleast 10"

        elif amount>=limit:
            return f"Dear customer you can't borrow {amount}is higher than a limit of {self.accountBalance}"

        else:
            self.loan+=amount
            return f"Dear customer {self.fullName} your loan of ksh{amount} has been granted successfully"

    def loan_repay(self,amount):
        if amount<self.loan:
            paying = self.loan-amount
            return f"Dear customer you have paid {amount} and your loan balance is {paying}"
        else:
            over_pay = amount-self.loan
            self.accountBalance+=over_pay
            return f"You have successfully completed paying your loan and the over pay is {over_pay} and your new balance is {self.accountBalance}"

    def transfer(self,amount,account):
        fee= amount*0.05
        Total=fee+amount
        if amount<0:
            return f"Dear customer {self.fullName} your amount is too low"
        elif Total>self.accountBalance:
            return f"Dear customer {self.fullName} you balance is {self.accountBalance} and you need atleast {Total}"
        else:
            self.accountBalance-=Total
            return f"Dear customer you  have sent {amount} to {account} and your new balance is {self.accountBalance}"