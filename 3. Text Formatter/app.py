s1=input('Enter String To do Text Formating ')
print('1. Upper Case')
print('2. Lower Case')
print('3. Title Case')
print('4. Sentence Case')
a=int(input('Enter option (1-4) '))
if(a==1):
    print(s1.upper())
elif(a==2):
    print(s1.lower())
elif(a==3):
    print(s1.title())
elif(a==4):
    print(s1.capitalize())
else:
    print('wrong Choice, your text is \n',s1)