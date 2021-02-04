import random

print("Time to play hangman!")
print("Start guessing...\n")
# A List Of Secret Words
with open('google-10000-english-usa-no-swears-long.txt') as f:
    words = f.read().split('\n')
word = random.choice(words)
guesses = ''
turns = 5
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end=""),
            failed += 1
    if failed == 0:
        print("\nYou won")
        break
    guess = input("\nguess a character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("\nWrong")
        print("\nYou have", + turns, 'more guesses')
        if turns == 0:
            print("\nYou Lose")
            print('The word is %s' % word)
