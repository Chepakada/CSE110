# for any boolean variable, the conditions should be written as in if statement
#for eg: s==a=10 or a==20
#the logical variable also has order; 
m=1
b=2
c=0
if m==1 or b==1 and c==2:
    print('okay')
else:
    print('Hi dummy:<')
#here the output is okay eventhough c==2
#but if c==2: is at front,
if  c==2 and m==1 or b==1 :
    print('okay')
else:
    print('Hi dummy:<')
    # here you are printed as hi dummy.