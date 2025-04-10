import random
import time

round=1
user_score=0
comp_score=0
game={1:'rock',2:'paper',3:'scissors'}
beats = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

def getName(a):
    if(a>3 or a<1):
        print('Wrong choice')
    else:
        return game[a]
    
def checkwinning(user1,user2):
    if(user1==user2):
        return 2
    elif(beats[user1] == user2):
        return 1
    else:
        return 0

def welcome():
    print(' Rock Paper Scissor Game 🎰'.center(100,'-'))
    print('  Rules ')
    print('- 👊🏻 Rock beat Scissor')
    print('- 🤚🏻 Paper beat Rock')
    print('- ✌🏻 Scissors beat Paper\n')

def main():
    global round
    global user_score
    global comp_score
    welcome()
    while(True):
        print()
        print(f' Round {round} '.center(100,'-'))
        print(f'Score Board: User {user_score} & Computer {comp_score}\n')
        print('1. Rock 👊🏻\n2. Paper 🤚🏻\n3. Scissor ✌🏻')
        try:
            num1= int(input('Enter No: '))
            if(num1 <1 or num1>3):
                print('Enter value between 1-3 ')
                continue
        except ValueError:
            print('Enter integer value')
            continue
        user_choice=getName(num1) 
        print('Computer Choosing',end="")
        for i in range(4):
            time.sleep(0.5)
            print('.',end="",flush=True)
        comp_choice=getName(random.randint(1,3))
        print(comp_choice)
        round+=1
        user_win= checkwinning(user_choice,comp_choice)
        comp_win= checkwinning(comp_choice,user_choice)
        if(user_win==1):
            user_score+=1
            print('User Win 🎉')
        elif(comp_win==1):
            comp_score+=1
            print('Computer Win 🎉')
        elif(user_win==2 and comp_win==2):
            print("It's Draw ⚔ 🤝🏻")
        if(user_score >=3 or comp_score>=3):
            if(user_score > comp_score):
                print('User Win Game 🎉😎')
            else:
                print('Computer Win Game 🎉💻')
            round=0
            user_score=0
            comp_score=0
            again=input('\nTry, again (yes/no) ')
            if(again.lower().strip() == 'yes' ):
                continue
            else:
                print('Goodbye ✋')
                break

main()