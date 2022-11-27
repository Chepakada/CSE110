import imp


import math
user_choice=int(input('How many rows and colums do you want? '))
row_col=user_choice+1
digits= int(math.log10(user_choice*user_choice))+1
for row in range(1, row_col):
    for col in range(1, row_col):
        print(f'{col*row:{digits}}', end=" ")
    print()
    