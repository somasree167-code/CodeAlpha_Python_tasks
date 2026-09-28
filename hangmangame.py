import random

words = ["python", "computer", "keyboard", "programming", "hangman", "apple", "planet"]

word = random.choice(words)
word_letters = set(word)
guessed_letters = set()
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while wrong_guesses < max_wrong:
    current_display = ""
    for letter in word:
        if letter in guessed_letters:
            current_display += letter + " "
        else:
            current_display += "_ "

    print("\nWord:", current_display)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word_letters:
        print("Correct!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1

    if all(letter in guessed_letters for letter in word_letters):
        print("\nCongratulations! You guessed the word:", word)
        break

else:
    print("\nGame over! The word was:", word)
