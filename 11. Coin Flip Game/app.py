import random
print(' Guess COIN Side 🧫'.center(100,'-'))
while (True):
    g=input('\nGuess coin side ')
    ch=['head','tail']
    r=random.choice(ch)
    g=g.lower().strip()
    
    if(not g):
        print('Wrong Choice')
        break
    elif (g not in ch):
        print('Please select between head or tail ♦')
        continue

    if(g==r):
        print(f'🎉 Correct Coin Guess: {g} 🧫')
    else:
        print(f'Coin show {r} 🧫')
        print(f'♦ Wrong Coin guess: {g} ')