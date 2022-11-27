
#As the stretch challenge one and 3 contradict eachother, first one is commented out in this code,/
#  if you want to go through it, please remove comments from exception1 

print('This is a extemely dangerous ride so, there are some QnA')
number=int(input('How many riders do you have(max two at a time)?'))
if number==1:
    age=int(input('What is your age?'))
    height=int(input('What is your height?(in inches please, and no unit!!)'))
    if age<18:
        gpass=input('Do you have a golden pass?(Y/N)').capitalize()
    if age>18:
        gpass='Y'
    person1 = age>=18 and height >=62 or gpass=="Y" and age>=12 and height>=62
    if person1==True:
        print('You can ride.')
    else:
        print('Sorry, you cannot ride..')

elif number==2:
    print('First person\'s info')
    age=int(input('What is your age?'))
    height=int(input('What in your height?(in inches please, and no unit!!)'))
    if age<18:
        gpass=input('Do you have a golden pass?(Y/N)').capitalize()
    else:
        gpass='Y'
    print('Second person\'s info')
    age1=int(input('What is your age?'))
    height1=int(input('What is your height?(in inches please, and no unit!!)'))
    if age1<18:
        gpass1=input('Do you have a golden pass?(Y/N)').capitalize()
    else:
        gpass1='Y'
    if age<age1:
        age1,age=age,age1
        height1,height=height,height1
    person1 = age>=18 and height >=62
    # the case of both being less than 18 but higher than 52 is  exception1 
    #This is for stretch one:----
    #exception1= age1>=12 and age>=12 and height >=52 and height1>=52
    #the case of one of them having pass is exception 2----
    exception2= age>=12 and gpass=='Y' and height>52
    #the case of another one of them having pass is exception2
    exception3= age1>=12 and gpass1=='Y' and height>52
    person2= height1>=36 and age1>18
    person= person1==True and person2== True #or exception1 ==True
    #the case where one of them is more than 16 and the other is more than 14
    exception4= age>=16 and age1>=14 and height>=52 and height1>=52
    #this is for both having pass or both matching age criteria
    if person==True or exception2==True and exception3==True:
        print('Both of you can ride.')
    #This is for both matching exceptional age criteria
    elif exception4==True:
        print('Both of you can ride.')
    #this is for one being older and another having pass
    elif person1==True and exception3==True:
        print('Both of you can ride.')
    #this is for one of them matching age critera
    elif person1==True: #and exception1==False:
        print('Only the older one can ride. Sorry about that. You gotta go alone.')
    #this is for either one of them having pass
    elif exception2== True or exception3==True:
        print('Only the person with pass can ride. Sorry about that. You gotta go alone.')
    #this is for them not matching any of the criteria
    else:
        print('Sorry, you cannot ride..')
else: 
    print('Only two at a time please!')
re=input('Next lot please. If you are there type Y').capitalize
    
    
