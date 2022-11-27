#The other day, I was really in trouble. It all started when I saw a very [adjective][animal][verb] down the hallway./
#  "Exclamation!"I yelled. But all I could think to do was to [verb] over and over./
#  Miraculously, that caused it to stop, but not before it tried to [verb] right infrot of my family. My family was [adjective] with me. /
# I tried stop them but [name] [animal]started to eat my [relation] /
# [body cloth] and then my family was really [adjective] that they[verb]me for 8 days.
adjective1=input('Please enter an adjective. ')
animal1=input('Please enter a name of an animal. ')
verb1=input('Please input a verb.(present participle) ')
n=input('Please input an exclamation. ')
exclamation=n.capitalize()
verb2=input('Please input a verb(simple present). ')
verb3=input('Please input a verb.(Simple present) ')
adjective2=input('Please input an adjective.')
name=input('Please input a name. ')
animal2=input('Please input a name of an animal. ')
relation=input('Please input a family relation. e.g. Sister, Mother. ')
clothes=input('Please input a body clothes. ')
adjective3=input('Please input an adjective. ')
verb4=input('Please input a verb.(simple past) ')
print(f'The other day, I was really in trouble. It all started when I saw a very {adjective1.lower()} {animal1.lower()} {verb1.lower()} down the hallway."{exclamation}!"I yelled. But all I could think to do was to {verb2.lower()} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3.lower()} right infrot of my family. My family was {adjective2.lower()} with me.  I tried stop them but {name.capitalize()}, my {animal2.lower()} started to eat my {relation.lower()}s  {clothes.lower()} and then my family was really {adjective3} that they {verb4} me for 8 days.')
input()

