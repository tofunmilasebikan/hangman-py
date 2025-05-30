import random

# ASCII hangman drawings
HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\\  |
    / \\  |
        ==='''
]

# Get a random word from the downloaded file
def get_word():
    try:
        with open("words_alpha.txt", "r") as file:
            words = [word.strip().upper() for word in file if word.isalpha() and len(word.strip()) >= 5]
            return random.choice(words)
    except FileNotFoundError:
        print("Error: 'words_alpha.txt' not found. Please download it from https://github.com/dwyl/english-words/raw/master/words_alpha.txt")
        exit()

# Show current word progress
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Main game loop
def hangman():
    word = get_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = len(HANGMAN_PICS) - 1

    print("Welcome to Hangman!\n")

    while wrong_guesses < max_wrong:
        print(HANGMAN_PICS[wrong_guesses])
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Used letters: {' '.join(sorted(guessed_letters))}")

        guess = input("Guess a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            print("❌ Wrong!")
            wrong_guesses += 1

        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 You guessed it! The word was: {word}")
            break
    else:
        print(HANGMAN_PICS[wrong_guesses])
        print(f"\n💀 Game Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
