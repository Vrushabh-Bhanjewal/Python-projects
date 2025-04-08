from functools import *
print('🏆 Grade Calculator 🏆')
marks=[]

# def calc(a,b):
#     return int(a) + int(b)
avg=0

while(True):
    a=input('Enter input Mark (or done)')
    if(a.isalpha()==True):
        a=a.lower().strip()

    if(a.isdigit()==True):
        marks.append(a)
        avg=reduce(lambda a,b: int(a)+int(b) , marks, 0) / len(marks)
        print('your average is: ',round(avg,2))
    elif(a=='done'):
            break  
    else:
        print('wrong choice')

print('Your marks are')
print(' '.join(marks))
print('\nYour average is: ',round(avg,2))
if(avg<=100 and avg >90):
    print('🥇 Grade: A+')
elif(avg<=90 and avg > 80):
    print('🥉 Grade: A')
elif(avg<=80 and avg > 70):
    print('🥈 Grade: B+')
elif(avg<=70 and avg > 60):
    print('🏅 Grade: C+')
elif(avg<=60 and avg > 50):
    print('🎖 Grade: C')
elif(avg<=50 and avg > 40):
    print('🎖 Grade: D')
elif(avg<=40 and avg > 30):
    print('📙 Grade: E')
elif(avg<=30 and avg > 0):
    print('♦ Grade: F')
else:
    print(f'Out of bound, Grade')
