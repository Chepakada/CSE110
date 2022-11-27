number=[]
addition=1
total=0
c=0
check=[]
low_positive=0
# built in funtion of total is sum
# built in function of max is max
#built in function of min is min
# c=count of input, number =list of numbers input addition = single element of list total= total count /
#  check= list of positive numbers  low_positive= lowest positive number

#algorithm
while addition!=0:
    addition=int(input('Enter a number.'))
    if addition==0:
        #this is method(when we use a list and then . and the a funtion, its method.)
        #this overwrites the list.
        #for not overwriting is to,---- number_sorted=sorted(number)
        number.sort()
        print(f'The sorted list is {number}')
    number.append(addition)
for n in number:
    total+=n
    c=c+1


#Don't you dare put check inside the for loop.
# what happened in here is, first all the positive numbers were grouped and then the lowest positive number is choosen.
#maybe there is another way to carry this out with less input---
#this is done by max(min for min).
#syntax is min(addition)

for y in number:
    if y>0:
        check.append(y)
        low_positive=y
        for z in check:
            if z<low_positive:
                low_positive=z

        
#c=c-1 because it counts c for 0 too.    
c=c-1


print(f'The mean of all the number that you input is {total/c:.2f}')
#print(c)    
print(f'The sum of all the numbers is {total}')    
print(f'The lowest positive number that you input is {low_positive}')