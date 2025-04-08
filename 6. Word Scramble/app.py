import random

print('\n🧩 Word Scramble 🧩\n'.center(100,'-'))
while True:
    str=input('Enter Word to Scramble: ')
    if(str.lower()=='quit'):
        break
    else:
        l=list(str) 
        random.shuffle(l) 
        print(''.join(l),'\n')
        # print(l)
print('Goodbye ')
