import random
import tools


def hangman():
    # Credits Hangman Ascii Art and wordbank:
    # https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c'''
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
            'coyote crow deer dog donkey duck eagle ferret fox frog goat '
            'goose hawk lion lizard llama mole monkey moose mouse mule newt '
            'otter owl panda parrot pigeon python rabbit ram rat raven '
            'rhino salmon seal shark sheep skunk sloth snake spider '
            'stork swan tiger toad trout turkey turtle weasel whale wolf '
            'wombat zebra ').split()

    word = random.choice(words)
    spaces = ['_'] * len(word)
    attemptsLimit = 7
    attempts = 0

    while True:
        tools.clear()

        print('Guess what the animal is: ')

        for space in spaces:
            print(space, end=" ")

        if attempts == 1:
            print(HANGMANPICS[0])
        elif attempts > 1:
            print(HANGMANPICS[attempts-1])

        print(f'Failed attempts [{attempts}]')

        letter = input('Letter: ')
        found = False

        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True

        if not found:
            attempts += 1

        if '_' not in spaces:
            tools.clear()
            print('You win 🥳')
            break

        if attempts == attemptsLimit:
            tools.clear()
            print('You lost 😖')
            print(HANGMANPICS[attemptsLimit-1])
            print('Word: ', word)
            break

        # to finish the game manually
        if letter == 'quit':
            break


if __name__ == '__main__':
    hangman()
