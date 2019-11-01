from time import time,sleep
class Hangman:
    def __init__(self, name, cart):
        self.name = name
        self.cart = cart

    def get_userinfo(self):
        self.name = input("What is your name? ")
        print(f"Hello {self.name}, let's to play hangman!\n\n")
        sleep(1)
        print("Ready...")
        sleep(0.5)

    def get_userinput(self):
        self.cart = "hangman"  #set the secret user_input
        guesses = '' #empty string to store string as they can be indiced & sliced and can work as a list also

        number_of_turns = 10
        while number_of_turns > 0:         
            failed_counter = 0 #loop to check the value                 
            for i in self.cart:      
                if i in guesses:    
                    print(i, end=" ")    
                else:
                    print("*", end=""),     
                    failed_counter += 1 
            if failed_counter == 0:        
                print ("You won") 
                break              

            guess = input("guess a character:") 

            guesses += guess # set the players guess to guesses
                            
            if guess not in self.cart:  
                number_of_turns -= 1        
                print ("Wrong")    
                print("You have", + number_of_turns, 'more guesses')
                if number_of_turns == 0:           
                    print("You Loose")  

player = Hangman('player', 'x')
player.get_userinfo()
player.get_userinput()
