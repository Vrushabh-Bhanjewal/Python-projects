print(' Reverse Name '.center(100,'-'))
while( True):
    str=input('\nEnter Name ')
    if(not str):
        break
    print('Reverse: ',str[::-1].capitalize())