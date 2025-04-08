
print('Unique Vowel Counter '.center(100,'-'))
vowel=['a','e','i','o','u']

while True:
    str=input('\nEnter string: ')
    if(str.lower()=='quit'):
        break
    l=list(str)
    count=0
    s=[]
    for i in l:
        if (i.lower() in vowel):
            count+=1
            s.append(i.lower())
            vowel.remove(i.lower())
    print(f'\nThere {count} Vowel in string')
    if(len(s) != 0):
        print(f'string contain { ", ".join(s) } Vowel')
print('Goodbye ')