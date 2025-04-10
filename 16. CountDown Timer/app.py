import time
print(' CountDown Timer '.center(100,'-'))
while(True):
    try:
        a=int(input('\nEnter Countdown Seconds: '))
        if(a > 0):
            while a!=0:
                print(f'{a} sec remaining... ')
                a-=1
                time.sleep(1)
            else:
                print('Timer Complete 🎉')
        else:
            print("Enter sec greter than zero ")
            continue
        ch=input('\nAdd another Timer(yes/no): ')
        if(ch.lower().strip()=='yes'):
            continue
        else:
            print('Goodbye ✋')
            break
    except ValueError:
        print('Add integer value')
        continue
    except:
        print('Force break occur')