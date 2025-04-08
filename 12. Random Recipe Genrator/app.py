from random import *
protein=['Chiken','Beef','Tofu','Fish','Eggs']
vegies=['broccoli','carrot','spinach','bell Paper','mushroom']
carbs=['rice','pasta','potato','quiona','bread']
methods=['baked','grilled','still-fried','roasted','sauteed']
flavours=['spicy','lemon','garlic','herb','sweet and sour']
emoji='🧆🥘🍲🍝🥣🥧🍷🍸🍹🍜🍛🍚🍱🥡🍗🍖🥗🥙🥪🌮🌯🥫🧀'

print(' Random Receipe Genrator '.center(100,'-'))
while True:
    str=input('\nGenrate some recipe (yes/no) '.title())
    if str.lower()=='no':
        print('Goodbye 😉')
        break
    elif(str.lower()=='yes'):
        recipe=f'{choice(protein)} {choice(methods)} {choice(protein)} with {choice(vegies)} and {choice(flavours)} {emoji[randint(0,len(emoji))]} '
        print(recipe)
    else:
        print('Wrong choice ')