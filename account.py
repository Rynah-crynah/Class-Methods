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
           return f"Hello {self.fullName} your deposited amount {amount} from {self.branch} and your new balance is {self.accountbalance}"    
        else:
            self.accountbalance+=amount
            self.deposits.append(amount)
            return f"Hello {self.fullName} you have deposited {amount} from {self.branch}. Your new balance is {self.accountbalance}"
   
    def withdraw(self, amount):
        if amount>self.accountbalance:
           return f"Hello {self.fullName} your balance is {self.accountbalance} from {self.branch},unfortunately, you cannot withdraw {amount}"
        elif amount<=0:
            return f"Amount must be greater than zero"
        else:
            self.accountbalance-=amount
            self.withdrawals.append(amount)
            return f"Hello {self.fullName} you have withdrawn {amount} from {self.branch} and your new balance is {self.accountbalance}"
       
    def deposits_statement(self):
          print(*self.deposits, sep="\n")  
         
    def withdrawals_statement(self):
        print(*self.withdrawals, sep="\n")      


    



 