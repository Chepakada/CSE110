from colorama import Fore, Back, Style  
from colorama import init

import time
init(autoreset=True)

list_items=[]
list_price=[]
list_item_quantity=[]
loop_vari=0
total=0
a=1




#The program starts here



print('Please do not press enter hastily, be patient and next option will come.')
print()
while loop_vari!=1:
    print(f'{Fore.CYAN}{Back.LIGHTRED_EX}The Shopping Cart.')
    print()
    print()
    print('Choose one of the following')
    
    print('1 for adding items to shopping list')
    print('2 for viewing shopping list.')
    print('3 for removing items from shopping list')
    print('4 for calculating the total')
    print('5 for quitting')
    choice=abs(int(input('Enter your choice.')))

    
    #The choice of adding the items.
    while choice==1:
        print('If you don\'t want anymore items, hit space once and then exit. ')
        item=input(f'{Fore.LIGHTYELLOW_EX}Enter the Item you want. ')
        if item==' ':
            break
        item_quantity=int(input(f'{Fore.RESET}{Back.RESET}{Style.BRIGHT} What quantity do you want? '))
        price=abs(float(input('Enter the price for a single unit.(If not in packets, follow SI system but do not enter the units. ')))
        print(f'You have successfully added {item} in the list. ')
        list_items.append(item)
        list_item_quantity.append(item_quantity)
        list_price.append(price)

    while choice==2:

        for i in range(len(list_items)):
            print(f'{i+1}.{Fore.LIGHTYELLOW_EX} {list_items[i]}{Fore.RESET}- {Style.BRIGHT}{list_item_quantity[i]}{Style.RESET_ALL} - {Fore.GREEN}{list_price[i]}{Fore.RESET}')    
        time.sleep(5)
        break



#the option of removing the item.
    while choice==3:
        print('If you don\'t want to remove items anymore, hit 0 once and then enter to exit. ')
        ind=int(input(f'{Fore.LIGHTYELLOW_EX}Enter the item number for the item you don\' want. '))
        #ritem_quantity=int(input(f'{Fore.RESET}{Back.RESET}{Style.BRIGHT} Enter the quantity quantity you want? '))
        #rprice=abs(float(input('Enter the price for a single unit.(If not in packets, follow SI system but do not enter the units. ')))
        ritem=list_items[ind-1]


        #if ritem_quantity==0:
        #this step is used for giving choice of reducing or increasing the quantity of items. Due to shortage of time, that hasn't been done.

        if ind!=0:
            list_items.remove(ritem)
            list_item_quantity.remove(list_item_quantity[ind])
            list_price.remove(list_price[ind])
            print(f'{Fore.GREEN}You have successfully removed {ritem} from the list.{Fore.RESET} ')

        else:
            break
        
                
            '''
            elif ritem_quantity!=0:
                list_item_quantity= list(map(lambda x: x.replace(list_item_quantity[ind], ritem_quantity), list_item_quantity))
                print(f'You have successfully reduced the {ritem} quantity to {ritem_quantity} ')
                break
            
            if ind==0:
                break
            '''
        



        
    #for calculating total
    while choice==4:
        for n in range(len(list_item_quantity)):
            total = total + list_item_quantity[n] * list_price[n]
        print(f'{Fore.CYAN}The total price you have to pay is {total}{Fore.RESET}')
        time.sleep(2)
        break
        


    #for quitting:
    if choice==5:
        print('Wait for 4 seconds. All the information saved will be cleared.')
        time.sleep(4)
        list_items=[]
        list_price=[]
        list_item_quantity=[]
        loop_vari=0
        total=0
        
        


    #the last
    if choice not in range(0,5):
        print(f'{Style.BRIGHT}INVALID INPUT!!{Style.RESET}')
        time.sleep(2)
        
#print('Thank you for shopping. Good bye')
#input()
            
            
            


    
    
    
    






   







