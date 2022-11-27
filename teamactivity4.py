from pydoc import locate

#Done finally!!!!!!!!!!!!!!!!!!!!!!
score=float(input('Please input your score.(you don\'t have to put the % sign.) '))
if score>=90:
    letter="A"
elif score>=80:
    letter="B"
elif score>=70:
    letter='C'
elif score>=60:
    letter='D'
else:
    letter='F'
scorent=score%10
if scorent==7 or scorent==8 or scorent==9:
    sign='+'
    if score>=96:
        sign=' '
elif scorent==1 or scorent==2 or scorent==3:
    sign='-'
    if score<=60:
        sign=' '
else:
    sign=' '
   
print(f'Your grade is {letter}{sign}')
if score < 70:
     print('You failed the class. But you can do better, a lot better.')
else:
    print('You passed your class')
input()

