import random
first=['Ghost','Fire','Moon','Sky','Ice','Shadow']
last=['Rider','Walker','Hunter','Seeker','Keeper','Dancer','Boomer']

print(' Name Genrator '.center(100,'-'))
a=int(input('Enter how many name you want '))
for _ in range(a):
    print(random.choice(first) + random.choice(last))
