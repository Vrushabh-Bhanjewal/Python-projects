from random import *
print(' Guess Scrambled Word '.center(100,'-'))
words = [
    "apple", "banana", "cherry", "dragonfruit", "elephant", "falcon", "giraffe", "harmony", "island", "jungle",
    "kite", "lemon", "mountain", "notebook", "ocean", "pencil", "quartz", "rainbow", "sunshine", "tiger",
    "umbrella", "violin", "whistle", "xylophone", "yogurt", "zebra"
]
while True:
    real=choice(words)
    sh=list(real)
    shuffle(sh)
    scram= "".join(sh)
    print(f'\nScrambled Word is 🧩 {scram}')
    word= input("what's the Word? ")
    if(word.lower().strip() ==real ):
        print('Congratulation 🎉, you guessed right ')
    else:
        print('Wrong Guess 📕')
    inp=input('Try again (yes/no)')
    if(inp.lower().strip() == 'yes'):
        continue
    else:
        print('Goodbye ✋')
        break