#This file contains the shopping list.
#price is the total price
#prices and items are useless
#item is the particular item of dictionary
# x is he corresponding value of item
from colorama import Fore, Back, Style  
import time




shoppinglist={
    }
def script():
    print('Choose one of the following')
    print('1 for viewing shopping list.')
    print('2 for adding items to shopping list')
    print('3 for removing items from shopping list')
    print('4 for calculating the total')
    print('5 for quitting')
    choice=int(input('Enter your choice.'))
    if choice==1:
        action=1
        while action!=2:
            added_item=input('Please input the item that you want to add.')
            if added_item==' ':
                action=2
            shoppinglist[added_item]=added_price
            print('If you are done, press space in next turn.')
            added_price=abs(float(input('Enter the price that you want to buy the item of. ')))
            
            



        




    '''
    #keep the algorithm sacred.
    price=0
    print(f'{Fore.GREEN}{shoppinglist}')
    time.sleep(0.2)
    item= 'hi'
    shoppinglist[' ']=0
    while item!=" ":
        item=input(f'{Style.DIM}{Fore.WHITE}Type the item you want.')
        x=shoppinglist[item]
        price=price+ x
    prices=shoppinglist.values()
    items=shoppinglist.items()
    time.sleep(1)

    print(f'{Fore.LIGHTGREEN_EX}Your total bill is {price}')

    '''
script()
action=1
#reloop=script()
#if reloop=='menu':
    #script()
    #print(shoppinglist)