import random
def choose_word():
 words = {"chromokopia", "Igor", "wolf"}
 return random.choice(words)

def display_word(word,guessed_letters):
    display = ""
    for letters in the word:
        if letter guessed_letters:
        else:
           display+= "_"
    return display
def hangman ():
   max_attempts = 6 guessed_letters = {}
   word_to_guess = choose_word()
   attempts = 0 

print("welcome to hangman")
print(display_word(word_to_guess, guessed_letters))

while true:
   