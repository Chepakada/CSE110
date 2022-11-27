print("Please enter the rates without % sign. For any meal other than the option below, it will be total of $7.5 and optio you choose.")
print('Child meal option 1 is $4.5.')
print('Child meal option 2 is $5.5.')
print('Child meal option 3 is $6.5.')
print('Child meal option 4 is $7.5.')
print('Adult meal option 1 is $6.5.')
print('Adult meal option 2 is $7.5.')
print('Adult meal option 3 is $8.5.')
print('Adult meal option 4 is $9.5.')
print('Adult meal option 5 is $10.5.')
print('Adult meal option 6 is $11.5.')
child1=int(input("What option of child's meal would you like to have today? "))
if child1 == 1:
    child=4.5
elif child1==2:
    child=5.5
elif child1==3:
    child=6.5
elif child1==4:
    child=7.5
elif child1==0:
    child=0
else:
    chlid=child1+4.5
adult1=int(input("What option of the adult's meal would you like to have today?"))
if adult1==1:
    adult = 6.5
elif adult1==2:
    adult=7.5
elif adult1==3:
    adult=8.5
elif adult1==4:
    adult=9.5
elif adult1==5:
    adult=10.5
elif adult1==6:
    adult=11.5
else:
    adult=adult1+7.5
childern_num=int(input("How many childerns are there? "))
if childern_num >= 3:
    print('Wow, that is a lot of childern.')
adult_number=int(input('How many adults are there?'))
input('Would you like some drinks?(They are complimentry)')
tax=float(input('Enter the tax ratio'))
print()
print()
subtotal= child*childern_num + adult*adult_number
salestax= subtotal*tax/100
total=subtotal+salestax
print(f'The subtotal is ${subtotal}.')
print(f'The tax is ${salestax}.')
print(f'The total you have to pay is ${total:.2f}.')
tips=input('Would you like to leave some tips good Sir?(Y/N) ')
if tips=='Y':
    tips_amt=float(input('How much would you like to leave? '))
    total_tips=tips_amt + total
else:
    total_tips=total
print()
print()
paybill=float(input('What bill are you going to pay? '))
print(f'your change is ${paybill - total_tips:.2f}')

input()