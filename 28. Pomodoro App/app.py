import os
import platform
import time

def clear_screen():
    if(platform.system()=='Windows'):
        os.system('cls')
    else:
        os.system('clear')

def format(sec):
    min=sec//60
    s=sec%60
    return f'{min:02d}:{s:02d}'

def countdown(sec,label):
    for remain in range(sec,0,-1):
        clear_screen()
        print(f'\n⌛ {label} ⏳\n')
        print("Time Remaining ⌚: ",format(remain))
        time.sleep(1)
    if(platform.system=='Windows'):
        import winsound
        winsound.Beep(1000,500)
    else:
        print('Alert 🔔')


def pomodoro():
    try:
        while(True):
            clear_screen()
            print('🍅 Pomodoro App 🍅'.center(100,'-'))
            print('Pomodoro Technique')
            print('- 25 min work\n- 5 min short break\n- 4 times repeat\n- 15 min long break')
            ch=input('\n would you like to use Default setting (yes/no) ').lower().strip()
            if(ch=='quit'):
                print('Goodbye✋🏻')
                break
            work_time=25
            short_break_time=5
            long_break__time=15
            repeat_count=4

            if(ch=='no'):
                while True:
                    try:
                        work_time=int(input('\nEnter Work Time (min) '))
                        short_break_time=int(input('Enter Short Break Time (min) '))
                        long_break__time=int(input('Enter Long Break Time (min) '))
                        repeat_count=int(input('Enter repeat count '))
                        if(work_time<=0 or short_break_time<=0 or long_break__time<=0 or repeat_count<=0):
                            print('\nEnter value greter than zero')
                            continue
                        break
                    except ValueError:
                        print('Enter Proper Value ')
                        continue
            work_sec=work_time*60
            short_sec=short_break_time*60
            long_sec=long_break__time*60
            while True:
                if(repeat_count<=0):
                    print('Repeat couunt Ended ',repeat_count)
                    break
                countdown(work_sec,'Keep Focusing')
                input('Work Session Completed\n Press Enter to start break')
                countdown(short_sec,'Take Rest')
                input('short Break Session Completed\n Press Enter for Next')
                repeat_count-=1
            countdown(long_sec,'take long break')
    except KeyboardInterrupt:
        print('Goodbye ✋🏻')

pomodoro()