
while(True):
    try:
        print(' 📅 Calculator 📅 '.center(100,'-'))
        print('\nSeclect Operation ')
        print('1. Addition\n2. Subtraction\n3. Multiplication\n4. Division')
        ch=int(input('Enter choice '))
        if(ch not in [1,2,3,4]):
            print('Wrong choice ')
            continue
        first=float(input('Enter First No '))
        sec=float(input('Enter Second No '))
        if(ch==4 and sec==0):
            print('Second no should not be zero')
            continue
        print() 
        if(ch==1):
            print(f'{first} + {sec} = {first+sec}')
        elif(ch==2):
            print(f'{first} - {sec} = {first-sec}')
        elif(ch==3):
            print(f'{first} * {sec} = {first*sec}')
        elif(ch==4):
            print(f'{first} / {sec} = {first/sec}')
    
        
        ch=input('\nDo, Another Operation (yes/no): ')
        if(ch.lower().strip()=='yes'):
            continue
        else:
            print('Goodbye ✋')
            break
    except ValueError:
        print('Wrong input ')
        continue
    