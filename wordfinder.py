FILE = "test.txt"
WORD_THRESHOLD = 3


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
    wordCountDict = count_words(filename)

    if len(wordCountDict) == 0:
        return None

    allWords = list(wordCountDict.keys())
    commonWordList = [allWords[0]]

    for currentword in wordCountDict:
        if wordCountDict[currentword] > wordCountDict[commonWordList[0]]:
            commonWordList.clear()
            commonWordList.append(currentword)

        elif wordCountDict[currentword] == wordCountDict[commonWordList[0]]:
            if currentword not in commonWordList:
                commonWordList.append(currentword)

    return commonWordList, wordCountDict[commonWordList[0]]


def result_message(commonWordAndFrequency):
    print("")

    if commonWordAndFrequency is None:
        print("There are no words in the file.")
        print("")
        return

    mostCommonWords = commonWordAndFrequency[0]
    wordFrequency = commonWordAndFrequency[1]

    if len(mostCommonWords) == 1:

        print("The most common word in '" + FILE + "' is: " + mostCommonWords[0])

        if wordFrequency == 1:
            print("'" + mostCommonWords[0].title() + "'" + " appears once.")
        else:
            print("'" + mostCommonWords[0].title() + "'" + " appears " + str(wordFrequency) + " times.")

        print("")

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
