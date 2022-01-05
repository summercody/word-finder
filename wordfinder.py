# This program imports a text file, parses the words in the file, and returns the most common word
# in the file as well as its frequency.

FILE = "test.txt"
WORD_THRESHOLD = 3


# Finds all the words in the text file and puts them into a dictionary
def count_words(filename):

    wordDict = {}

    with open(filename) as f:
        for line in f:
            line = line.strip("\n")
            words = line.split(" ")
            for word in words:
                word = word.strip("(),.;'/-")
                word = word.lower()
                if word.isalpha() and len(word) >= WORD_THRESHOLD and word != "and" and word != "the":
                    if word not in wordDict:
                        wordDict[word] = 1
                    else:
                        wordDict[word] += 1

    return wordDict


def common_word_finder(filename):

    # Create a dictionary of all the words and their frequencies
    wordCountDict = count_words(filename)

    # Return if the dictionary is emtpy -- the file contains no words
    if len(wordCountDict) == 0:
        return None

    # Make a list of all the words in the dictionary. Store the first word in the list in a secondary
    # list, which will keep track of the word (or words, if there is a tie) that appear most frequently
    allWords = list(wordCountDict.keys())
    commonWordList = [allWords[0]]

    # Cycle through all the words in the dictionary, and store the word(s) with the greatest
    # frequency in the common word list
    for currentword in wordCountDict:

        # If the current words appears more frequently than the first word in the
        # common word list, empty the list input the current word
        if wordCountDict[currentword] > wordCountDict[commonWordList[0]]:
            commonWordList.clear()
            commonWordList.append(currentword)

        # If the current word appears with the same frequency as the first word in the common word
        # list, add the current word to the list
        elif wordCountDict[currentword] == wordCountDict[commonWordList[0]]:
            if currentword not in commonWordList:
                commonWordList.append(currentword)

    # Return a tuple with the list of most common words and their frequency
    return commonWordList, wordCountDict[commonWordList[0]]


def result_message(commonWordAndFrequency):
    print("")

    # Result message if there are no words in the file
    if commonWordAndFrequency is None:
        print("There are no words in the file.")
        print("")
        return

    # Store the most common words and their frequency in two variables
    mostCommonWords = commonWordAndFrequency[0]
    wordFrequency = commonWordAndFrequency[1]

    # If only one word appears with the greatest frequency
    if len(mostCommonWords) == 1:

        print("The most common word in '" + FILE + "' is: " + mostCommonWords[0])

        if wordFrequency == 1:
            print("'" + mostCommonWords[0].title() + "'" + " appears once.")
        else:
            print("'" + mostCommonWords[0].title() + "'" + " appears " + str(wordFrequency) + " times.")

        print("")

    # If multiple words tie for the most common word
    else:

        print("The most common words in '" + FILE + "' are: " + str(mostCommonWords).strip("[]").replace("'", ""))

        if wordFrequency == 1:
            print("Each word appears once.")
        else:
            print("Each word appears " + str(wordFrequency) + " times.")

        print("")


def main():
    commonWordsAndFrequency = common_word_finder(FILE)

    result_message(commonWordsAndFrequency)


if __name__ == '__main__':
    main()
