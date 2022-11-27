import math
ages=[]
names=['bill','tom','sue']
ages.append(12)
ages.append(10)
ages.append(20)
ages.append(40)
print(f'{ages=}')


#names.append(('Hello','bello','cello','mello'))
names.append('jill')
print(f'{names=}')
n=0
for age in ages:
    n=age+n
print(n)
for name in names:
    print(name)
print(ages[1])
print(ages)