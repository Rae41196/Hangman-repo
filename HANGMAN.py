from time import time,sleep
class Hangman:
    def __init__(self, name, user_input):
        self.name = name
        self.user_input = user_input

    def get_userinfo(self):
        self.name = input("What is your name? ")
        print(f"Hello {self.name}, let's to play hangman!\n\n")
        sleep(1)
        print("Ready...")
        sleep(0.5)

    def get_userinput(self):
        self.user_input = "hangman"  #set the secret user_input
        guesses = '' #empty variable to store letters   remember to create a list

        number_of_turns = 10
        while number_of_turns > 0:         
            failed_counter = 0 #loop to check the value                 
            for i in self.user_input:      
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
                            
            if guess not in self.user_input:  
                number_of_turns -= 1        
                print ("Wrong")    
                print("You have", + number_of_turns, 'more guesses')
                if number_of_turns == 0:           
                    print("You Loose")  

player = Hangman('player', 'x')
player.get_userinfo()
player.get_userinput()
