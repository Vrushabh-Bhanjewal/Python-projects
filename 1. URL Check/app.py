print('Website URL Checker\n')
url= input('Enter Website URL: ')
if(url.startswith('https://')):
    print('This website use https (Secure ✔)')
elif(url.startswith('http://')):
    print('This website use https (not Secure X)')
else:
    print('Look like its not Website ')