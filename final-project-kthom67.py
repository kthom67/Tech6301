class BankAccount:

    def __init__(self, name, accountType, balance=0):
        import random
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = random.randint(1,99999999)
        self.filename = str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"
        file = open(self.filename, "w")
        file.write("Account number:\n"+str(self.accountNumber)+"\n"+"Name:\n"+str(self.name) + "\n" + "Account type:\n" + str(self.accountType) + "\n" + "Starting balance:\n" + str(self.balance)+ "\n"+ "Current balance:\n"+str(self.balance)+ "\n")
        file.close()
    def Deposit(self, amount):
        self.amount=amount
        self.fileName = str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"
        self.accountFile=open(self.fileName, "r")
        self.fileLines= self.accountFile.readlines()
        self.accountFile.close()
        self.currentbalance=int(self.fileLines[9])
        self.newbalance=int(self.currentbalance)+int(self.amount)
        self.fileLines[9]=str(self.newbalance)+"\n"
        self.fileLines.append("Deposit:\n")
        self.fileLines.append(str(self.amount)+"\n")
        self.file = open(self.fileName, "w")
        for self.line in self.fileLines:
            self.file.write(str(self.line))
        self.file.close()

    def Withdraw(self, amount):
        self.amount = amount
        self.fileName = str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"
        self.accountFile = open(self.fileName, "r")
        self.fileLines = self.accountFile.readlines()
        self.accountFile.close()
        self.currentbalance = int(self.fileLines[9])
        if self.currentbalance >= self.amount:
            self.newbalance = int(self.currentbalance) - int(self.amount)
            self.fileLines[9] = str(self.newbalance) + "\n"
            self.fileLines.append("Withdrawal:\n")
            self.fileLines.append(str(self.amount) + "\n")
            self.file = open(self.fileName, "w")
            for self.line in self.fileLines:
                self.file.write(str(self.line))
            self.file.close()
        else:
            print("No, not enough money and no overdraft.")
    def Balance(self):
        self.fileName = str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"
        self.accountFile = open(self.fileName, "r")
        self.fileLines = self.accountFile.readlines()
        self.currentbalance=int(self.fileLines[9])
        print(self.currentbalance)
        return self.currentbalance
    def getuserID(self):
        print(self.accountNumber)
        return self.accountNumber

    def getname(self):
        print(self.name)
        return self.name

    def gettype(self):
        print(self.accountType)
        return self.accountType
    def transactions(self):
        self.fileName = str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"
        self.accountFile=open(self.fileName, "r")
        self.fileLines= self.accountFile.readlines()
        self.history=self.fileLines[10:]
        for self.line in self.history:
            print(self.line)
        self.file.close()

account1=BankAccount(name="peter", accountType="chequing", balance=0)
account2=BankAccount(name="kristi", accountType="chequing", balance=5)
account2.Deposit(3)
account2.Deposit(37)
account2.Deposit(1)
account2.Balance()
account2.Withdraw(1)
account2.Balance()
account2.Withdraw(500)
account1.getuserID()
account2.getname()
account2.transactions()
