import random
choice='yes'
play_again=choice!='yes'
count=0
guess=-1
while choice=='yes':
    magic_no=random.randint(1,100)
    while guess!=magic_no:
        guess=int(input('Guess the magic number'))
        count=count+1
        if magic_no<guess:
            print('Guess lower')
        elif magic_no>guess:
            print('Go higher')
        else:
            print('You guessed right')
    print(f'Your total attempt was {count}')
    choice=input('Do you want to play agian?').lower()
print('Thank you for playing.')




