import random

def get_random_word():
    words = ["python", "java", "kotlin", "javascript", "hangman", "developer", "programming"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    return stages[tries]

def play_hangman():
    word = get_random_word()
    word_letters = set(word)
    guessed_letters = set()
    correct_letters = set()
    tries = 6

    print("Let's play Hangman!")
    
    while tries > 0 and word_letters != correct_letters:
        print(display_hangman(tries))
        print(f"Guessed letters: {' '.join(guessed_letters)}")
        
        word_display = [letter if letter in correct_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_display))
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            correct_letters.add(guess)
            guessed_letters.add(guess)
        else:
            guessed_letters.add(guess)
            tries -= 1
            print(f"Incorrect guess. You have {tries} tries left.")
    
    if word_letters == correct_letters:
        print(f"Congratulations! You've guessed the word '{word}'!")
    else:
        print(display_hangman(tries))
        print(f"Sorry, you've run out of tries. The word was '{word}'.")

play_hangman()
