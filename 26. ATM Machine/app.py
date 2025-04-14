# ?----------------------------

from datetime import *
import time
import pickle

class wrongType(Exception):
    def __init__(self,msg):
        print(msg)
class minimum(Exception):
    def __init__(self,msg):
        print(msg)

class User():
    def __init__(self,name,pin,balance=0,hist=[]):
        self.name=name
        self.pin=pin
        self.balance=balance
        self.hist=hist

    def withdraw(self,amt):
        try:
            if(amt<0):
                raise minimum('Withdraw Amount should be higher than zero')
            elif(amt >= self.balance):
                print('withdraw amount is higher than balance ')
            elif(self.balance  <  (amt + 1500)):
                print('Account should have Minimum 1500rs deposite')
                print('you can withdraw upto ',self.balance-1500)
            else:
                self.balance-=amt
                self.hist.append([f'Withdraw - {amt} rs',datetime.now()])
                print(f'Amount Withdraw {amt} rs')
        except minimum:
            pass

    def deposite(self,amt):
        try:
            if(amt > 0):
                self.balance+=amt
                self.hist.append([f'Deposite + {amt} rs',datetime.now()])
                print(f'Amount Deposited + {amt} rs')
            else:
                raise minimum('Amount should be higher than zero ')
        except minimum:
            pass
    def checkBalance(self):
        print("Balance: ",self.balance)

    def changePin(self,code):
        self.pin=code
        print('Pin Changed')
      
    def statement(self):
        print('\n','='.center(100,'='))
        print(f'Name:{self.name} ')
        print(f'Current Time: {datetime.now()}\n')
        print('Transactions\t\t\t Time')
        print(''.center(100,'-'))
        for mess in user.hist:
            print(f'{mess[0]} \t\t {mess[1]}')
        print('='.center(100,'='),"\n")

class ATM:
    def __init__(self):
        self.file_name = 'data.txt'
        self.users_data = self.loadData()

    def loadData(self):
        try:
            with open(self.file_name,'rb') as f:
                users= pickle.load(f)
        except:
            users=[]
            print('No user data Found, starting new')
        return users

    def saveData(self):
        with open(self.file_name,'wb') as f:
            pickle.dump(self.users_data,f)
    def pinCheck(self,pin):
        attempt=0
        for i in range(3):
                    guest_pin= int(input(('Enter pin: ')))
                    if(pin==guest_pin):
                        return True
                    else:
                        attempt += 1
                        print(f'Wrong pin, Attempt: {attempt}')
                        if(attempt >=3 ):
                            print('Your 3 Attempt over')
                            return False
                        continue 
    def newUser(self):
        print('Please Provide some Personal details ')
        name=input('Enter Your Name: ')
        name=name.lower().strip()
        amount=int(input('Enter initial Amount in balance: '))
        pin=int(input('Enter Pin: '))
        new_user = User(name,pin,amount,[['Account Created ',datetime.now()]] )
        self.users_data.append(new_user)
        self.saveData()
        print('user created succesfully\n')
        return new_user

    def existingUser(self):
        if not self.users_data:
            print('No Existing User Present')
            return None
        guest=input('Enter User Name: ')
        guest=guest.lower().strip()
        for user in self.users_data:
            if(user.name==guest):
                print('Data Fetching...')
                time.sleep(1)
                print('Match Found\n')
                password=self.pinCheck(user.pin)
                if(password==True):
                    print(f'Welcome back, {user.name}')
                    return user
                else:
                    return None            
        print('No User Found')
        return None          
        
    def AtmMenu(self,user):
        while(True):
            print(" ATM ".center(100,'-'))
            print("1. Check Balance" )
            print("2. Deposite Money" )
            print("3. Withdraw Money" )
            print("4. Change Pin" )
            print('5. Mini Statement')
            print('6. Exit\n')
            try:
                choice= int(input('Enter Choice No: '))
                if(choice==1):
                    user.checkBalance()
                elif(choice==2):
                    amt=int(input('Enter amount to Deposite '))
                    user.deposite(amt)
                elif(choice==3):
                    amt=int(input('Enter amount to Withdraw '))
                    user.withdraw(amt)
                elif(choice==4):
                    password=self.pinCheck(user.pin)
                    if(password):
                        code=int(input('Enter new Pin: '))
                        user.changePin(code)
                    else:
                        continue
                elif(choice==5):
                    user.statement()
                elif(choice == 6):
                    print('saving data...')
                    self.saveData()
                    break
                else:
                    continue
            except ValueError:
                print('wrong choice ')
            finally:
                self.saveData()

while(True):
    a1 = ATM()
    print('\nWelcome to ###### ATM Machine ') 
    choice=input('Are You new User (yes/no) ') 
    yes_choice=['yes','YES','Y','y','Yes','True','true','1']
    no_choice=['no','NO','No','N','n','False','false','0']
    if(choice in yes_choice ): 
        user= a1.newUser()
    elif(choice in no_choice):
        user=a1.existingUser()
        if user==None:
            continue
    elif(choice.lower().strip()=='quit'):
        break
    else:
        print('wrong choice')
        continue
    a1.AtmMenu(user)
