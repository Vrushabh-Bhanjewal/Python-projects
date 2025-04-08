print('🥾 Steps Counter 🥾\n')
goal=int(input('Enter Steps Count Daily Goal: '))
count=int(input('Enter today Steps Count '))
if(goal > count):
    print(f'You need more {goal-count} steps to reach Goal of {goal} 🥾')
elif(goal < count):
    print(f'Congratulation 🎉, You have exceed goal by {count-goal} steps! 🥾 ')
else:
    print(f'Congratulation🎉, You reached your {goal} goal 🥾')
