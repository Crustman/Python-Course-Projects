import random

print("Welcome to the hangman game!!")
words = ["hacker", "bounty", "random"] 
secret_word = random.choice(words)
#print(secret_word)
print("You get 5 Guess")
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)
    

num = 0
game_over = False

while not game_over:
    guess = input("Guess a letter ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]   
        if letter == guess:
            display_word[position] = letter 
    if guess not in secret_word:
        num += 1
        guess_left = 5 - num
        print(f"You have {guess_left} guesses left")
        if num >= 5:
            print("You Loser")
            game_over = True    
              
    print(display_word)
        
    if "_" not in display_word:
        print("You Win!!!")     
        game_over = True      
   