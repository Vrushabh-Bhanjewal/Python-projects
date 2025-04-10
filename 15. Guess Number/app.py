from random import *
print(' Guess Number (1-100) 🧿'.center(100,'-'))
print('You have 10 attempt to Guess ')

while(True):
    num=randint(1,100)
    game_over=False
    count=0
    while count<10 or not game_over:
        try:
            inp=int(input(f'\nGuess No: '))
            count+=1
            if count==10:
                print(f'\nNumber was {num} 🧿')
                game_over=True

            if(inp<num):
                print(f'Your No is to low  📈 attempt {count}')
                continue
            elif(inp>num):
                print(f'Your No is to high 📉 attempt {count}')
                continue
            else:     
                print(f'Congratulation🎉 , You Guessed {num} 🧿 Right in attempt {count}')
                break
        except ValueError:
            print('Enter integer value ')
            continue
    ch=input('Try again (yes/no)')
    if(ch.lower().strip()=='yes'):

        continue
    elif(ch.lower().strip()=='no'):
        game_over=True
        print('Goodbye ✋')
        break
    else:
        print('Wrong Choice ')
        break
