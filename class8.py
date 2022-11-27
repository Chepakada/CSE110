#in range(), the first number inside the bracket nmeans starting point nad second means the ending whereas third is steps it jumps
'''
range(1,5)
for i in range(1,5):
    print(i, end=" ")

number=int(input('How many times: '))
for i in range(number):
    print(f'hello, {i}')


print()
my_string='Have a nice day.'
for letter in my_string:
    print(letter, end="")

    print(    )
    my_list=[1,2,3,4,5]
    for x in my_list:
        print(x)
        '''
'''
for i in range(1,5):
    print('i loop:', i)
    for j in range(6,9):
        print('j loop is: ', j, end=' ')
        print()
'''
number=int(input('How many rows and columns do you want in your multiplication table? '))
for i in range(1, number+1):
    for r in range(1, number+1):
        num= i * r
        print(num, end = ' ')
    print()