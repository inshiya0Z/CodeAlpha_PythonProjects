import random

# List of predefined words
words = ["apple", "table", "chair", "plant", "house"]
chosen_word = random.choice(words)

# Variables
guessed_word = ["_"] * len(chosen_word)
guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman!")
print("Guess the word letter by letter.")

while attempts > 0 and "_" in guessed_word:
    print("\nWord: " + " ".join(guessed_word))
    print(f"Guessed Letters: {', '.join(guessed_letters)}")
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Correct!")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong!")
        attempts -= 1
        print(f"Attempts left: {attempts}")

# End of game
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game Over! The word was:", chosen_word)