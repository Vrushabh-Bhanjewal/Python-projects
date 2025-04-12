import re

def getinput():
    lines=[]
    print(' - Press Enter to stop')
    print('Enter Text to Analyze ')
    while True:
        data=input(' > ')
        if(data==''):
            break
        lines.append(data)
    text=' '.join(lines)
    print('Your Text is📑: ',text)
    return text

def analyse(str):
    alpha_count=len(re.findall('[a-zA-Z]',str,re.IGNORECASE))
    digit_count=len(re.findall('[0-9]',str,re.IGNORECASE))
    special_count=len(re.findall('\W',str,re.IGNORECASE))
    space_count=len(re.findall('\s',str,re.IGNORECASE))
    # word count
    word_count=len(re.findall(r'\b\w+\b',str))
    # Sentence count
    sc=0
    s=['!','.','?']
    for i in str:
        if(i in s):
            sc+=1
    if(sc==0 and str.strip()):
        sc=1
    # word per sentence
    if(sc >0):
        ws=word_count/sc
    else:
        ws=0
    print('\nAlphabates Count: ',alpha_count)
    print("Digit Count     : ",digit_count)
    print("special Count   : ",special_count)
    print("space Count     : ",space_count)
    print("word Count      : ",word_count)
    print("sentence Count  : ",sc)

def main():
    while(True):
        print('🔎📑 Text Analyzer 📑🔍'.center(100,'-'))
        print('\n1. Text Analyzer\n2. Exit')
        try:
            ch=int(input('Enter choice '))
        except ValueError:
            print('Wrong input')
            continue
        if(ch==1):
            data= getinput()
            analyse(data)
        elif(ch==2):
            print('Goodbye,✋🏻')
            break
        else:
            print('Please enter choice between 1 or 2 ')
            continue
    
main()