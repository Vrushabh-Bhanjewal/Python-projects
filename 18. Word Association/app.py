import time
import random
word_associations = {
    "sun": (["star", "book", "car", "pizza"], 0),
    "apple": (["chair", "fruit", "phone", "pen"], 1),
    "car": (["banana", "river", "vehicle", "moon"], 2),
    "book": (["mountain", "read", "light", "chess"], 1),
    "rain": (["hat", "fire", "shoe", "umbrella"], 3),
    "music": (["spoon", "dog", "song", "ball"], 2),
    "computer": (["tree", "guitar", "mountain", "technology"], 3),
    "fire": (["flame", "ice cream", "chair", "desk"], 0),
    "school": (["game", "ocean", "television", "student"], 3),
    "money": (["cash", "cloud", "egg", "blanket"], 0),
    "phone": (["carpet", "candle", "call", "cup"], 2),
    "tree": (["book", "forest", "microwave", "hat"], 1),
    "beach": (["snow", "mountain", "sand", "pencil"], 2),
    "coffee": (["mug", "orange", "glove", "shoe"], 0),
    "dog": (["cat", "rocket", "bus", "table"], 0),
}
score=0
round=0
print(' Word Association Game '.center(100,'-'))
while(True):
    prim = random.choice(list(word_associations.keys()))
    start=time.time()
    print('\nEnter word associated with given string between options📗: ')
    print('Word is : ',prim)
    count=0
    for i in word_associations[prim][0]:
        count+=1
        print(count,". ",i)
    ch=input('Enter associated word 📘 ')
    end=time.time()
    ans=word_associations[prim][0][word_associations[prim][1]]
    print(ans)
    round+=1
    if(ch.lower().strip() == ans):
        print('\ncorrect answer 🎉')
        point=int(max(1,5-(end-start)))
        score+=point
        print(f'Your current point is {point}/5 ')
        print(f'Your Total score is {score}/{round*5}')
    else:
        print('\nWrong answer🧨, it was:',ans)
    print('Round: ',round)
    print('Your Response Time was ',end-start)
    again=input('\nTry, again (yes/no) ')
    if(again.lower().strip() == 'yes' ):
        continue
    else:
        print('Goodbye ✋')
        break
    
    
