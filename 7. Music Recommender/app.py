import random
genre={
    'rock':['AC/DC','Queen','Led Zepplin'],
    'pop':['Taylor Swift','Ed Sheeren','Ariana Grande'],
    'hip-hop':['Kendrick Lamar','Drake','J.Cole']
}
print(' Music Recommender '.center(100,'-'))
str=input(('Enter music genres (rock,pop,hip-hop) '))
if(str not in genre):
    print('Sorry, no song added for this song')
else:
    print('Try, ',random.choice(genre[str.lower().strip()] ))
    