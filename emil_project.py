import random
def choose_word():
 words = {"chromokopia", "Igor", "wolf"}
 return random.choice(words)

def display_word(word,guessed_letters):
    display = ""
    for letters in word:
        if letter guessed_letters:
      
       else:
          display+= "_"
    return display
def hangman ():
   max_attempts = 6 
   guessed_letters = {}
   word_to_guess = choose_word()
   attempts = 0 


print("welcome to hangman")
print(display_word(word_to_guess, guessed_letters))
guess = input ("guess a letter").lower()
if guess.isalpha() and len () guess == 1: 
      elif guess in guessed_letters:
   guessed_letters.append (guess)
    print ("good guess!")
else:
   print ("incorrect guess, attempts remaining:"), max_attempts - attempts 

print ("invalid input, please enter a single letter")
print  (display_word(word_to_guess, guessed_letters))

if set(guessed_letters == set (word_to_guess):
       print  ("congratulations you guessed the firt word")
   if attempts == max_attempts:
   print ("sorry you run out of attempts, the word was:")
while true:
   if max_attempts > 6:
      break