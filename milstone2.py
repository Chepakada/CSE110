def script():
    from colorama import Fore, Back, Style
    from colorama import init
    import time
    init(autoreset=True)
    print(f'{Fore.RED}WELCOME TO THE ADVENTURE OF CANAL JUMPERS!')
    print("-"*44)
    print()
    print()
    energy=5
    store=5
    print(f'{Fore.BLUE}{Style.BRIGHT}It is a simple game where you can choose the equipment you may need to kill the monsters in canal, jump the canal and replenish your energy.')
    print(f'{Fore.GREEN}Your every choice costs you energy and the more efficient the choice the lesser the health but you may charge replenish your energy by eating the item you collect.')
    print(f'{Fore.BLACK}{Style.DIM}Anything typed on GREEN is your choice, type that to choose it')
    input(f'{Fore.LIGHTBLACK_EX} Hit enter if you are ready to start.')

    print(f'{Back.YELLOW}It your front, there is a {Fore.GREEN}ENERGY BAR,{Fore.RED} a {Fore.GREEN}PIKE {Fore.RED} and a {Fore.GREEN}JUMP POLE,{Fore.RED} choose what you want.')
    choice_one=input().lower()
    while choice_one !='energy bar' and choice_one !='pike' and choice_one !='jump pole':
        choice_one=input("That was an invalid input, try again: ").lower()
    if choice_one=='energy bar':
        energy=energy+1
    elif choice_one=="pike":
        store=store-1
    elif choice_one=='jump pole':
        store=store-2
        
    print('-')
    time.sleep(1)
    print('--')
    time.sleep(1)
    print('---')
    time.sleep(1)
    print(f'{Back.YELLOW}Nice choice. Lets move some steps move some steps towards the Canal.')
    print(f'{Back.YELLOW}Wow, items are flying around today. There is a {Fore.GREEN}shield {Fore.RED} and a {Fore.GREEN}jump pole,{Fore.RED} what do you wanna pick? ')   
         
    choice_two=str(input().lower())
    while choice_two!='shield'and choice_two!='jump pole':
        choice_two=str(input('Invalid Input. Plese try again:').lower())
    if choice_two=='shield':
        store=store+2
    elif choice_two=='jump pole':
        store=store+1
    print(f'{Back.CYAN}Uhoo. The canal. Opps there is a huge snake there..')
    choice_three=str(input(f'{Back.YELLOW}Do you want to {Fore.GREEN} fight{Fore.RED} it or {Fore.GREEN} jump {Fore.RED} over from here?').lower())
    result_one=[choice_one,choice_two]
    if choice_three=='fight':
        if 'shield'in result_one and 'pike' in result_one:
            print('-')
            time.sleep(1)
            print('--')
            time.sleep(0.5)
            print(f'{Back.YELLOW}Wow, you killed the snake.')
            energy=energy-2
            print(f'Your energy is getting low, you need to search for some energy bars. Or you could eat the shell that you got after killing snake, it will make you full.')
        elif 'sheild' in result_one and 'energy bar' in result_one:
            print('-*-')
            time.sleep(1)
            print('*-*')
            time.sleep(0.5)
            print('..')
            time.sleep(0.5)
            print(f'{Back.YELLOW}Wow, that was a tough battle, you are drenched of your health, eat your energy bar or you will die soon.')
            energy=energy-4
            eat_or_die=input(f'{Back.RED}Would you like to eat your energy bar?{Fore.GREEN}(y/n)')
            time.sleep(1)
            if eat_or_die=='y':
                print(f'{Back.RED}You, nearly survived.{Back.BLACK}')
            else:
                print('.....')
                time.sleep(0.5)
                print('...')
                time.sleep(0.5)
                print('.') 
                time.sleep(0.4)
                return "death"
                #print('you die...')
                anything=input(f'{Fore.BLUE}{Style.DIM}Do you want to restart the game or exit reinput?{Fore.GREEN}(y/n/re)')
                if anything == 'y':
                    script()
                elif anything=='re':
                    script()
                else:
                    exit()
        elif 'pike'in result_one and 'jumping pole' in result_one:
            print(f'{Back.CYAN}{Fore.WHITE}You have killed the snake but lost its crystal. Good job, the villagers will praise you.')
            energy=energy-2
        else:
            energy=energy-3
            print(f'{Fore.BLACK}{Style.DIM}It was a fool\'s endevour. The only way for you to survive is if you run back and never come back')
            choice_three_2=input(f'Do you still want to cross the canal or rest for healing.{Fore.GREEN}(y/n)').lower()
            if choice_three_2=='y':
                print('-'*10)
                time.sleep(1)
                print('-'*5)
                time.sleep(0.5)
                print(f'You are healed a little bit. Now you can cross the river.')
            else:
                print(':( '*3)
                time.sleep(0.2)
                print(':| '*3)
                time.sleep(0.5)
                print('You die.')
                input()
                anything=input(f'{Fore.BLUE}{Style.DIM}Do you want to restart the game or exit reinput?{Fore.GREEN}(y/n/re)')
                if anything == 'y':
                    script()
                elif anything=='re':
                    script()
                else:
                    exit()
    elif choice_three=='jump':
        if 'jump pole'in result_one and 'energy bar' in result_one:
            print(f'{Fore.RED}Nice jump buddy, did not see that on you.')
            energy=energy-1
        elif 'jump pole'in result_one and 'shield' in result_one:
            print(f'{Fore.RED}That was a near one, glad you survived.')
            energy=energy-2
        elif 'pike' in result_one and 'jump pole' in result_one:
            print(f'{Fore.RED}Not bad buddy, not bad.')
            energy=energy-1
        elif 'jump pole' and 'jump pole' in result_one:
            print(f'{Fore.RED}Wow, that was AMAZING.')
        elif "shield" and 'energy bar' in result_one:
            print(f'{Fore.Red}Sorry man, you couldn\'t make the jump.')
            print(':( '*3)
            time.sleep(0.2)
            print(':| '*3)
            time.sleep(0.5)
            return 'death'
        else:
            print(f'{Fore.Red}Sorry man, you couldn\'t make the jump.')
            print(':( '*3)
            time.sleep(0.2)
            print(':| '*3)
            time.sleep(0.5)
            print('You die.')
            input()
            anything=input(f'{Fore.BLUE}{Style.DIM}Do you want to restart the game or exit reinput?{Fore.GREEN}(y/n/re)')
            if anything == 'y':
                script()
            elif anything=='re':
                script()
            else:
                exit()
    print('It has been a long journey, Rest for a bit, after you rest, we will come up with another part for the game. Till then, good bye.') 
    input()    
ending = script()
if ending == "death":
    print("You died")

while ending=='death':
    ch1=input('do you wanna restart the game?(y/n)').lower
    if ch1=='y':
        ending = script()