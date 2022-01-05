"""
This program is called "Word Finder". It reads a given text file, parses the text into
individual words, and calculates which word (or words) appear most frequently. From there,
the user can either request the word(s) directly, or play a guessing game to figure out the most
common word themselves.
"""

# Load a given text file. The name of the text file is requested at the start of the program.
FILE = None

# The number of letters required for a string of text to be considered a word
WORD_THRESHOLD = 3


# A function that reads through a text file and loads each word into a dictionary, keeping track of
# how many times each word appears. This dictionary gets returned at the end.
def parse_words(filename):

    # A dictionary that keeps track of the words in a given text file, as well as their frequencies.
    wordDict = {}

    # Open the text file
    with open(filename) as f:

        # Parse through each line, stripping all non-alphabet and non-numerical
        # characters and making each word lowercase
        for line in f:
            line = line.strip("\n")
            words = line.split(" ")

            for word in words:
                word = word.strip("(),.;'/-")
                word = word.lower()

                # If the word only consists of letters, meets the word threshold, and is
                # neither "and" nor "the", then load it into the dictionary.
                if word.isalpha() and len(word) >= WORD_THRESHOLD and word != "and" and word != "the":

                    # Check if the word is already in the dictionary. If not, add it.
                    if word not in wordDict:
                        wordDict[word] = 1

                    # If so, increase the word's frequency by 1.
                    else:
                        wordDict[word] += 1

    return wordDict


# A function that cycles through the dictionary returned by "parse_words", and figures out which word(s)
# appear most frequently. The function returns a tuple containing a list of the most common word(s), and
# the frequency with which those words appear.
def common_word_finder(filename):

    # Load the dictionary returned by "parse_words"
    wordCountDict = parse_words(filename)

    # If there are no words in the text file, return with the value "None"
    if len(wordCountDict) == 0:
        return None

    # Load a list of all the keys from the dictionary -- which are all of the words -- into the variable
    allWords = list(wordCountDict.keys())

    # Load the first word from the word list into the variable. Keeps track of the most common words in the file
    mostCommonWordList = [allWords[0]]

    # Cycle through each word in the word dictionary, and check their frequencies
    for currentword in wordCountDict:

        # If the current word appears more frequently than the first word in the mostCommonWordList,
        # empty the list and insert the current word
        if wordCountDict[currentword] > wordCountDict[mostCommonWordList[0]]:
            mostCommonWordList.clear()
            mostCommonWordList.append(currentword)

        # If the current word appears as frequently as the first word in the mostCommonWordList,
        # add the current word to the list
        elif wordCountDict[currentword] == wordCountDict[mostCommonWordList[0]]:
            if currentword not in mostCommonWordList:
                mostCommonWordList.append(currentword)

    # Store the frequency of the first word from the list (which should be equivalent to the frequency of
    # all other words in the list) into the variable
    wordFrequency = wordCountDict[mostCommonWordList[0]]

    # return the list of most common words, and their frequency
    return mostCommonWordList, wordFrequency


# Runs a game in which the user guesses the most common word in a text file. If there is
# more than one most common word, the function will use the first word in the list returned by
# "common_word_finder", and make note of the other common words once the game is completed.
def play_game(commonWordAndFrequency):

    print("")

    # If there are no words in the file
    if commonWordAndFrequency is None:
        print("There are no words in the file.")
        print("")
        return

    # Pull the list of most common words from the tuple, and store it in the variable
    mostCommonWords = commonWordAndFrequency[0]

    # Pull the frequency of the most common words from the tuple, and store it in the variable
    wordFrequency = commonWordAndFrequency[1]

    # Pull the first word from the list of most common words, and store it in the variable
    firstWord = mostCommonWords[0]

    guess = input("Guess the most common word in '" + FILE + "'. Hit 'Enter' by itself at any point to end the game and"
                                                             " return to the start menu: ")

    # Keeps track of how many guesses the user has made
    guess_counter = 1

    # Keeps track of how many guesses the user has left
    guesses_left = 9

    # While the user has neither guessed the most common word nor hit 'Enter' to quit,
    # prompt them for the correct word, giving hints along the way
    while guess != firstWord and guess != "":

        if guess_counter <= 2:
            print("")
            guess = input("Sorry, guess again! You have " + str(guesses_left) + " guesses left. Hint -- the word has " + str(len(firstWord)) + " letters. ")
            guess_counter += 1
            guesses_left -= 1

        elif 2 < guess_counter <= 5:
            print("")
            guess = input("Sorry, guess again! You have " + str(guesses_left) + " guesses left. Hint -- the word has " + str(
                len(firstWord)) + " letters and starts with the letter '" + str(firstWord[0]) + "'. ")
            guess_counter += 1
            guesses_left -= 1

        elif 5 < guess_counter <= 7:
            print("")
            guess = input("Sorry, guess again! You have " + str(guesses_left) + " guesses left. Hint -- the word has " + str(
                len(firstWord)) + " letters and starts with the letters '" + str(firstWord[0:2]) + "'. ")
            guess_counter += 1
            guesses_left -= 1

        elif 7 < guess_counter <= 9:
            print("")
            guess = input("Sorry, guess again! You have " + str(guesses_left) + " guesses left. Hint -- the word has " + str(
                len(firstWord)) + " letters and starts with the letters '" + str(firstWord[0:3]) + "'. ")
            guess_counter += 1
            guesses_left -= 1

        # If the user has hit 10 guesses, reveal the most common word(s) and exit the function
        elif guess_counter >= 10:
            print("")
            print("Sorry, the word was: " + firstWord + ". It appears " + str(wordFrequency) + " times.")

            # If there is one other word that is equally as common
            if len(mostCommonWords) == 2:
                print("The other most common word in this file is: " + str(mostCommonWords[1]))

            # If there is more than one word that is equally as common
            elif len(mostCommonWords) > 2:
                print("The other most common words in this file are: " + str(mostCommonWords[1:]).strip("[]").replace("'", ""))

            return

    # If the user hits 'Enter', quit the program and return to the start menu
    if guess == "":
        print("")
        print("Game Over.")
        display_user_options(commonWordAndFrequency)

    # If the user has successfully guessed the most common word, print a congratulatory message
    else:
        print("")
        print("Well done! The most common word in '" + FILE + "' is: '" + mostCommonWords[0] + "'. It appears " + str(wordFrequency) + " times.")

        # If there is one other word that is equally as common
        if len(mostCommonWords) == 2:
            print("The other most common word in this file is: " + str(mostCommonWords[1]))

        # If there is more than one word that is equally as common
        elif len(mostCommonWords) > 2:
            print("The other most common words in this file are: " + str(mostCommonWords[1:]).strip("[]").replace("'", ""))


# If the user requests the most common word directly, without playing the guessing game, this function
# will print the most common word(s) from the provided text file.
def word_find_result_message(commonWordAndFrequency):
    print("")

    # If there are no words in the file
    if commonWordAndFrequency is None:
        print("There are no words in the file.")
        print("")
        return

    # Pull the list of most common words from the tuple, and store it in the variable
    mostCommonWords = commonWordAndFrequency[0]

    # Pull the frequency of the most common words from the tuple, and store it in the variable
    wordFrequency = commonWordAndFrequency[1]

    # If there is only one word in the list
    if len(mostCommonWords) == 1:

        print("The most common word in '" + FILE + "' is: " + mostCommonWords[0])

        # If the word appears only once
        if wordFrequency == 1:
            print("'" + mostCommonWords[0].title() + "'" + " appears once.")

        # If the word appears more than once
        else:
            print("'" + mostCommonWords[0].title() + "'" + " appears " + str(wordFrequency) + " times.")

        print("")

    # If there is more than one word in the list
    else:

        print("The most common words in '" + FILE + "' are: " + str(mostCommonWords).strip("[]").replace("'", ""))

        # If the words appears only once
        if wordFrequency == 1:
            print("Each word appears once.")

        # If the words appear more than once
        else:
            print("Each word appears " + str(wordFrequency) + " times.")

        print("")


# This function takes in user input and decides whether to run the guessing game, display the most
# common word(s) directly, or quit the program.
def display_user_options(wordInfo):

    print("")

    # Display the introductory message, and store the user's choice
    choice = input("Hi, welcome to Word Finder! "
                   "To find the most commonly used word in your text document, "
                   "type 'Find'. To guess the most commonly used word, "
                   "type 'Play'. Or, hit 'Enter' to end the program. ")

    # If the user does not chose a valid command, prompt the user until they do
    while choice != "Play" and choice != "Find" and choice != "":
        print("")
        choice = input("Sorry, please enter a valid command. Or, hit 'Enter' to end the program. ")

    # If the user responds "Find", run the function "word_find_result" and
    # display the most common words on the console
    if choice == "Find":
        word_find_result_message(wordInfo)

    # If the user responds "Play", run the function "play_game" and begin the word finder
    # guessing game
    elif choice == "Play":
        play_game(wordInfo)

    # If the user hits 'Enter', print a closing message and quit the program
    elif choice == "":
        print("")
        print("See you later!")
        quit()


def main():
    global FILE

    # Request the name of the desired text file from the user
    FILE = str(input("Please enter the name of your text file, including its extension (Example: 'test.txt'). "
                     "Or, hit 'Enter' to quit: "))

    # If the user hits 'Enter' as opposed to entering a file name, quit the program
    if FILE == "":
        quit()

    # Parse the text file, and load both the list of most common words and their frequency into the
    # provided variable.
    commonWordsAndFrequency = common_word_finder(FILE)

    # Give the user the option to receive the word(s), play a guessing game, or quit the
    # program.
    display_user_options(commonWordsAndFrequency)


if __name__ == '__main__':
    main()
