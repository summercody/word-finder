# word-finder

This repository contains two programs, "wordfinder" and "wordfindergame", both of which are word-search based programs written in Python. It also contains two text files that can be used to test each programs' functionality. 

"wordfinder" reads a text file, parses all of its words, and prints the file's most commonly used word(s) to the console. 

"wordfindergame" builds upon the code in "wordfinder" and creates a game in which users can guess what the most common word in a given text file might be. The game is played via the console.


NB: both programs decide what items are considered words using a constant, WORD_THRESHOLD. The constant checks for how many characters are in the word after parsing. The default value is set to 3 characters, though it can be changed to make the program more or less sensitive.