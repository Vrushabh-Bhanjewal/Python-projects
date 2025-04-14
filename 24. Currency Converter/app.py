import requests
import time
import threading

API_KEY='6eafc8a25e2d60406f68f1aa'
list_site='https://api.currencyfreaks.com/v2.0/currency-symbols'

def converter():
    print('\nSome Popular Currency option like ')
    print('USD, EUR, GBP, JPY, CAD, AUD, CNY, INR \n') 
    while True:   
        cfrom =input('\nCountry Currency Code From: ').upper().strip()
        if(cfrom not in res):
            print('Invalid Currency Name ')
            continue
        cto =input('Country Currency Code To: ').upper().strip()
        if(cto not in res):
            print('Invalid Currency Name ')
            continue
        break
    amount=int(input(f'Enter {cfrom} amount to Convert '))
    search_site=f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{cfrom}'
    try:
        search_res=getAPIData(search_site)['conversion_rates']
        res_to=search_res[cto]
        conv_amt=res_to*amount
        print(f'\n✨ Coverting {cfrom} TO {cto} Amount {amount}: {round(conv_amt,3)}\n')
    except KeyError:
        print('\n❌ Sorry, look like currency not available in API data\n')
    except:
        print('Look like some error occur in API Data')

    
def getAPIData(list_site):
    try:
        resp=requests.get(list_site)
        res=resp.json()
        print('Wait moment fetching Data',end="")
        for _ in range(3):
            time.sleep(0.5)
            print('.',end="",flush=True)
        print()
        return res
    except:
        print('Problem occur while fetching data...')
        return {} 

def main():
    global res
    while(True):
        print('🧫 Currency Converter 🧫'.center(100,'-'))
        print('\n1. Currency Converter \n2. List Of Currency\n3. Exit')
        try:
            ch=int(input('Enter choice '))
        except ValueError:
            print('Wrong input')
            continue
        if(ch==1):
            converter()
        if(ch==2):
            count=0
            for a,b in res.items():
                count+=1
                print(count,".",a,"\t :",b)
        elif(ch==3):
            print('Goodbye,✋🏻')
            break
        else:
            print('Please enter choice between (1-3) ')
            continue

res=getAPIData(list_site)['currencySymbols']        
main()