name = input("What is your name? ")
print(f"Hello {name}, let's to play hangman!\n\n")
print("Ready...")

word = "hangman" #set the secret word
guesses = ''#create empty value


#determine the number of turns
number_of_turns = 10
while number_of_turns > 0:         
    failed_counter = 0 #loop to check the value                 
    for i in word:      
        if i in guesses:    
             print(i, end=" ")    
        else:
            print("*", end=" "),     
            failed_counter += 1 
    if failed_counter == 0:        
        print ("You won") 
        break              

    guess = input("guess a character:") 

    guesses += guess # set the players guess to guesses
                    
    if guess not in word:  
        number_of_turns -= 1        
        print ("Wrong")    
        print("You have", + number_of_turns, 'more guesses')
        if number_of_turns == 0:           
            print("You Loose")  