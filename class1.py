###variables (and good names)
#create a string variable
from types import new_class


first_name ="John"

#create an integer variabe
age = 29
user_age= input('enter your age ')
user_age=int(user_age)

#float is the number wiht decimal
age2=int(input('enter your age: '))
pi=float(input('enter the value of y '))

fave_flavor=input('what flavor icecream do you want')
num_scoops=int(input('how many scoops do you want?'))
print('hello', first_name, 'I will get you' , num_scoops, " of", fave_flavor, 'icecream')
#output all the variables again, but use a string method on one
# so that it prints in upper case, lower case, or title case
print(f"hello {first_name.upper()} i'll get you {num_scoops} scoops of  {fave_flavor.title()} ice cream." )


print('.'*10)
