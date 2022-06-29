file = open(r"D:\HARI\coding\Budget_App\data.txt","r+")
val=file.readlines()
class Budget:
    def __init__(self,name):
        self.name=name
        
class Entertainment(Budget):
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,deposit):
        self.balance = self.balance+deposit
        val[0]=str(self.balance)+"\n"
    def withdraw(self,withdraw):
        if self.balance > withdraw:
            self.balance = self.balance - withdraw
            val[0]=str(self.balance)+"\n"
        else:
            print("No Fund")
        
class Food(Budget):
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,deposit):
        self.balance = self.balance+deposit
        val[1]=str(self.balance)+"\n"
    def withdraw(self,withdaw):
        if self.balance > withdaw:
            self.balance = self.balance - withdaw
            val[1]=str(self.balance)+"\n"
        else:
            print("No Fund")

class Clothes(Budget):
    def __init__(self, balance):
        self.balance = balance
    def deposit(self,deposit):
        self.balance = self.balance+deposit
        val[2]=str(self.balance)+"\n"
    def withdraw(self,withdraw):
        if self.balance > withdraw:
            self.balance = self.balance - withdraw
            val[2]=str(self.balance)+"\n"
        else:
            print("No Fund") 
ent = Entertainment(int(val[0]))
fd= Food(int(val[1]))
clth=Clothes(int(val[2]))

x=int(input("1.Entertainment\n2.Food\n3.clothes"))
if x ==1:
    y=int(input("1.Deposit\n2.Withdraw\n3.Balance"))
    if y==1:
        ent.deposit(int(input("Enter the amount to deposit:")))
    elif y==2:
        ent.withdraw(int(input("Enter the amount to Withdraw:")))
    elif y ==3:
        print(ent.balance)
elif x ==2:
    y=int(input("1.Deposit\n2.Withdraw\n3.Balance"))
    if y==1:
        fd.deposit(int(input("Enter the amount to deposit:")))
    elif y==2:
        fd.withdraw(int(input("Enter the amount to Withdraw:")))
    elif y ==3:
        print(fd.balance)
elif x ==3:
    y=int(input("1.Deposit\n2.Withdraw\n3.Balance"))
    if y==1:
        clth.deposit(int(input("Enter the amount to deposit:")))
    elif y==2:
        clth.withdraw(int(input("Enter the amount to Withdraw:")))
    elif y ==3:
        print(clth.balance)
print(val)
file.seek(0)
file.truncate(0)
file.writelines(val)
file.close()