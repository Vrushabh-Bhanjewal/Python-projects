import string
import re
from random import *

def getinput():
    while(True):
        try:
            print('\n 📑 Fulfill Requirement for Genrating Password ')
            p_len=int(input('Enter length of password (min:8 and max:30) '))
            if(p_len<8 or p_len>30):
                print('length should between (8-30) ')
                continue
            use_alpha=input('Do you want Alphabates in password (yes/no)').lower().strip()
            if(use_alpha!='no'):
                use_alpha=True
            use_digit=input('Do you want Digits in password (yes/no)').lower().strip()
            if(use_digit!='no'):
                use_digit=True
            use_punc=input('Do you want Special Character in password (yes/no)').lower().strip()
            if(use_punc!='no'):
                use_punc=True
            return(p_len,use_alpha,use_digit,use_punc)
        except ValueError:
            print('Enter integer value')
            continue
        except:
            print('error occurd')
            continue
    
def getpassword():
    pl,use_alpha,use_digit,use_punc=getinput()
    print(pl,use_alpha,use_digit,use_punc)
    chars=''
    if(use_alpha==True):
        chars+=string.ascii_lowercase+string.ascii_uppercase
    if(use_digit==True):
        chars+=string.digits
    if(use_punc==True):
        chars+=string.punctuation
    if(chars==''):
        print('\n ⭕ Look like Nothing selected\n By default alphabates 🆎 will be selected')
        chars+=string.ascii_lowercase+string.ascii_uppercase
    pass1=''.join(choices(chars,k=pl))
    print('\n 🔑 Password:',pass1,"\n")
    return pass1

def checkstrength(pass1):
    grade=0
    a1=re.findall(fr'[{pass1}]',string.ascii_lowercase+string.ascii_uppercase)
    if(len(a1)>3):
        grade+=4
    d1=re.findall(fr'[{pass1}]',string.digits)
    if(len(d1)>2):
        grade+=2
    p1=re.findall(fr'[{pass1}]',string.punctuation)
    if(len(p1)>2 ):
        grade+=2

    if(len(a1)!=0):
        print('Alphabates check  ✅')
    if(len(d1)!=0):
        print('Digit check       ✅')
    if(len(p1)!=0):
        print('Punctuation check ✅')
    print()

    if(grade >6):
        print(' 🔥 Excellent Strength ')
    if(grade <=6 and grade>2):
        print(' 💥 Good Strength ')
    if(grade <=2 and grade>0):
        print('🔁 I think you should try again ')
    print(grade)

def main():
    while(True):
        print('🔏 Password Genrator 🔐🔏🔓🔒🔑🗝'.center(100,'-'))
        print('\n1. Create Password\n2. Exit')
        try:
            ch=int(input('Enter choice '))
        except ValueError:
            print('Wrong input')
            continue
        if(ch==1):
            pass1 = getpassword()
            checkstrength(pass1)
        elif(ch==2):
            print('Goodbye,✋🏻')
            break
        else:
            print('Please enter choice between 1 or 2 ')
            continue

main()