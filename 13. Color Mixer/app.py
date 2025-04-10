from random import *

c_mixer={
    ('red','blue'):'purple',
    ('red,yellow'):'orange',
    ('blue','yellow'):'green',
    ('blue','green'):'teal',
    ('white','red'):'pink',
    ('red','green'):'brown'
}
print('🎨 Color mixer 🎨'.center(100,'-'))
while(True):
    mix=input('\nTry mixing Colors (yes/no) ')
    if(mix.lower()=='yes'):
        str1=input('Enter 1st color ')
        str2=input('Enter 2nd color ')
        if((str1.lower().strip(),str2.lower().strip() ) not in c_mixer):
            print('Color not added in data ')
            continue
        color=c_mixer[(str1.lower().strip(),str2.lower().strip() )]
        print(f'Your mix color is {color} 🎨🖌')
        
    elif(mix.lower()=='no'):
        print('Goodbye, Artist  🖌')
        break
    elif(str()):
        print('Wrong choice ')
        continue
        