str=input('Enter single character ')
a=str[0]
if(a.isalpha()==True):
    print(f'{a} is letter')
elif(a.isdigit()==True):
    print(f'{a} is digit')
elif(a.isspace()==True):
    print('char is space')
else:
    print(f'{a} is special charcter')
