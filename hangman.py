import random
def display_hangman(wrong_guesses):
  #Displays the hangman visual based on incorrect guesses
  stages = [
      #  empty
      """
          --------
          |      | 
          |
          |
          |
          -
      """,
      #  head
      """
          --------
          |      |
          |      O
          |
          |
          -
      """,
      #  head, torso
      """
          --------
          |      |
          |      O
          |     /
          |
          -
      """,
       #  head, torso, one arm
      """
          --------
          |      |
          |      O
          |     /|
          |
          -
      """,
      #  head, torso, both arms
      """
          --------
          |      |
          |      O
          |     /|\ 
          |
          -
      """,
      #  head, torso, both arms, one leg
      """
          --------
          |      |
          |      O
          |     /|\ 
          |     / 
          -
      """,
      #  head, torso, both arms, both legs
      """
          --------
          |      |
          |      O
          |     /|\ 
          |     / \ 
          -
      """   
  ]
  print(stages[wrong_guesses-1])

def get_word(category):
  #Selects a random word from a specific category
  word_lists = {
      "fruits": ["apple", "banana", "orange", "mango", "strawberry"],
      "animals": ["dog", "cat", "elephant", "lion", "tiger"],
      "countries": ["india", "usa", "canada", "china", "australia"],
      "professions": ["doctor", "teacher", "engineer", "lawyer", "programmer"]
  }
  return random.choice(word_lists.get(category, [])).lower()

def choose_difficulty():
  #Prompts the user to select a difficulty level
  while True:
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    if difficulty in ("easy", "medium", "hard"):
      return difficulty
    else:
      print("Invalid difficulty. Please choose easy, medium, or hard.")

def play(word):
  #Main game loop for Hangman
  wrong_guesses = 0
  word_completion = ["_" for _ in word]  # Create a list with underscores for hidden letters
  guessed_letters = []
  max_guesses = {
      "easy": 7,
      "medium": 5,
      "hard": 3
  }

  # Main game loop
  while wrong_guesses < max_guesses[difficulty] and "_" in word_completion:
    print(" ".join(word_completion))
    print(f"You have {max_guesses[difficulty] - wrong_guesses} wrong guesses left.")

    # Get user input
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
      print("Invalid input. Please enter a single letter.")
      continue
    elif guess in guessed_letters:
      print("You already guessed that letter.")
      continue

    guessed_letters.append(guess)

    # Check if guess is in the word
    if guess in word:
      # Update word completion
      for i in range(len(word)):
        if word[i] == guess:
          word_completion[i] = guess
    else:
      wrong_guesses += 1
      display_hangman(wrong_guesses)

  # Check win or lose condition
  if "_" not in word_completion:
    print(f"Congratulations! You guessed the word: {word}")
  else:
    print(f"You ran out of guesses. The word was: {word}")

# Start the game
difficulty = choose_difficulty()
category = input("Choose category (fruits/animals/countries/professions): ").lower()
word = get_word(category)
play(word)
