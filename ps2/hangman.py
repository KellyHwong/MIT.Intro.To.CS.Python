# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    # print("  ", len(wordlist), "words loaded.")
    print(len(wordlist), "words loaded.")

    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
# Global variant
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letter_perm = []
    for l in secret_word:
        if l not in letter_perm:
            letter_perm.append(l)
    # All in letter_perm

    for l in letters_guessed:
        if l in letter_perm:
            letter_perm.remove(l) # remove all, but letter permutation

    if len(letter_perm) == 0:
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letter_perm = []
    for l in secret_word:
        if l not in letter_perm:
            letter_perm.append(l)
    # All in letter_perm

    for l in letters_guessed:
        if l in letter_perm:
            letter_perm.remove(l) # remove all, but letter permutation

    # left letters in letter_perm are not guessed
    # not guessed, guessed
    # replace letters in word that not guessed with "_ "
    show_string = ""
    for l in secret_word:
        if l in letter_perm:
            show_string += "_ "
        else:
            show_string += l
    return show_string


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    # print(string.ascii_lowercase)
    all_lowercase = string.ascii_lowercase
    for l in letters_guessed:
        all_lowercase = all_lowercase.replace(l, "")
    return all_lowercase
    
def printWarning(warnings_left):
    if warnings_left > 0:
        print("You have %d warnings left: " %warnings_left, end = "")
    else:
        print("You have no warnings left so you lose one guess:", end = "")

    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    letters_guessed = []
    available_letters = string.ascii_lowercase
    warnings_left = 3
    guesses_left = 6
    print("I am thinking of a word that is %d letters long." %len(secret_word))
    print("You have %d warnings left." %warnings_left)

    while True:
        # round start
        print("-------------")
        if guesses_left == 0:
            print("Sorry, you ran out of guesses. The word was else.")
            break

        print("You have %d guesses left." %guesses_left)
        print("Available letters: " + available_letters)
        letter = input("Please guess a letter:")
        # just one letter please
        if len(letter) > 1:
            print("Please input only one letter", end = "")
            warnings_left -= 1
            printWarning(warnings_left)
            print(get_guessed_word(secret_word, letters_guessed))
            continue
        # in lowercase letters
        if letter not in string.ascii_lowercase:
            print("Oops! That is not a valid letter.", end = "")
            warnings_left -= 1
            printWarning(warnings_left)
            print(get_guessed_word(secret_word, letters_guessed))
            continue
        # already guessed
        if letter in letters_guessed:
            print("Oops! You've already guessed that letter.", end = "")
            warnings_left -= 1
            printWarning(warnings_left)
            print(get_guessed_word(secret_word, letters_guessed))
            continue

        # finally got a correct guess
        guesses_left -= 1
        letters_guessed.append(letter)
        available_letters = available_letters.replace(letter, "")

        if letter in secret_word:
            print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))

        if warnings_left == 0:
            break

        



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '')
    if not len(my_word) == len(other_word):
        return False
    else:

        for i in range(len(my_word)):
            if not (my_word[i] == other_word[i] or my_word[i] == '_'):
                return False
        
        return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)

    if len(possible_matches) == 0:
        print("No matches found")
    else:
        print("Possible word matches are:")
        print(possible_matches)

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    letters_guessed = []
    available_letters = string.ascii_lowercase
    warnings_left = 3
    guesses_left = 6
    print("I am thinking of a word that is %d letters long." %len(secret_word))
    print("You have %d warnings left." %warnings_left)

    while True:
        # round start
        print("-------------")
        if guesses_left == 0:
            print("Sorry, you ran out of guesses. The word was else.")
            break

        print("You have %d guesses left." %guesses_left)
        print("Available letters: " + available_letters)
        letter = input("Please guess a letter:")
        # deal with hint
        if letter == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
        # just one letter please
        if len(letter) > 1:
            print("Please input only one letter", end = "")
            warnings_left -= 1
            printWarning(warnings_left)
            print(get_guessed_word(secret_word, letters_guessed))
            continue
        # in lowercase letters
        if letter not in string.ascii_lowercase:
            print("Oops! That is not a valid letter.", end = "")
            warnings_left -= 1
            printWarning(warnings_left)
            print(get_guessed_word(secret_word, letters_guessed))
            continue
        # already guessed
        if letter in letters_guessed:
            print("Oops! You've already guessed that letter.", end = "")
            warnings_left -= 1
            printWarning(warnings_left)
            print(get_guessed_word(secret_word, letters_guessed))
            continue

        # finally got a correct guess
        guesses_left -= 1
        letters_guessed.append(letter)
        available_letters = available_letters.replace(letter, "")

        if letter in secret_word:
            print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))

        if warnings_left == 0:
            break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    # secret_word = 'apple'
    # letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    # letters_guessed = ['e', 'i', 'k', 'p', 'r', 's', 'a', 'l']
    # print(is_word_guessed(secret_word, letters_guessed))
    # print(get_guessed_word(secret_word, letters_guessed))
    # print(get_available_letters(letters_guessed))
    # secret_word = choose_word(wordlist)
    secret_word = "apple"
    # hangman(secret_word)
    hangman_with_hints(secret_word)
    # print(match_with_gaps("te_ t", "tact"))
    # print(match_with_gaps("a_ _ le", "banana"))
    # print(match_with_gaps("a_ _ le", "apple"))
    # print(match_with_gaps("t_ _ t", "take"))
    # show_possible_matches("t_ _ t")
    # show_possible_matches("abbbb_ ")
    # show_possible_matches("a_ pl_ ")

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
