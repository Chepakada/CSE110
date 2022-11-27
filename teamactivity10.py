bank_names=[]
bank_balances=[]
loop=0
ave=0
max_num_ind=0
a=0
print('If you want to quit, enter "quit"')
while loop==0:
    name=input('Enter the name of bank account. ').lower()
    if name=='quit':
        break
    balance=float(input('Enter the bank balance. '))
   
    bank_names.append(name)
    bank_balances.append(balance)
#bank_names.remove('quit')
#bank_balances.pop()
for i in range(len(bank_names)):
    print(f'{bank_names[i]} - {bank_balances[i]}')
for i in range(len(bank_balances)):
    ave += bank_balances[i]
print(f'The average bank balance is {ave/len(bank_balances)}')
print(f'The total amount you have is {ave}')
'''
max_bank_balances=max(bank_balances)
max_bank_balances_index=bank_balances.count(max_bank_balances)
print(max_bank_balances_index)
print(max_bank_balances)
'''
'''
for i in bank_balances:
    if i>0:
        y=bank_balances(i)
        max_num_ind=y
        
print(bank_names(max_num_ind))
'''
a=bank_balances.index(max(bank_balances))
print(a)
print(f'the heighest account is {bank_names[a]} with bank ac name {bank_balances[a]}')


