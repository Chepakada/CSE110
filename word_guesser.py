guess_word = "goldman"

word_collector = ""
for i in guess_word:
    word_collector = "_"*len(guess_word)

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])
counter = 0
while word_collector != guess_word:
    print(word_collector)
    user_input = str(input("Input your guess?"))  
    
    if user_input in guess_word:
        user_input_index = guess_word.index(user_input)
        
        
        word_collector = replace_str_index(word_collector, user_input_index, user_input)
        
    else:
        counter = counter + 1
        print ("try again")

print("you found your guess work")    
print(f"You took {counter+1} attemps")


