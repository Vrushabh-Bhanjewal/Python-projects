import os
import random
import time

round=1
nums=[]
over=False

print('✨ Rules ✨')
print(' - Watch number appear one by one ')
print(' - After sequence shown type in order they come')
print(' - Each round add one more number')
print(' - How far can you go\n')
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def digit():
    return random.randint(0,9)
input('Press Enter to start ')

while not over:
    clear()
    print(f' Round {round} '.center(100,'-'))
    print('Remember sequence of Number ')
    nums.append(digit())
    for i in nums:
        print(i)
        time.sleep(1)
        clear()
    data=input('Enter No seprated by space ')
    user=[int(i) for i in data.split()]
    # print(user)
    if(nums == user):
        round+=1
        print(f'congratulation, you guessed {round} right No 🎉')
        continue
    else:
        print(f'look like you guessed wrong 🧨, upto {round-1} Round')
        print(' '.join(str(i) for i in nums)) 
        nums=[]
    again=input('\nTry, again (yes/no) ')
    if(again.lower().strip() == 'yes' ):
        continue
    else:
        print('Goodbye ✋')
        over=True
        # break
