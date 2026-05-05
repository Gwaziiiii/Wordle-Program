# Wordle program!
import random



def getWord():

    wordList = ["APPLE", "SPRAY", "PAINT", "BREAK", "CRANE", "LOOPS", "FLANK", "FRIED", "TRUST", "BRING",
                "CRAVE", "PANTS", "GRAPE", "ELATE", "OCEAN", "SNIFF", "CRANK", "BELLY", "YOUNG", "TOUCH",
                "UNITY", "FLOOD", "CATCH", "ASHES", "ANTSY", "SOUPS", "FISHY", "FALSE", "WRONG", "EQUAL",
                "MOODY", "FEEDS", "INNER", "CAPES", "SPARK", "LOCAL", "CRUEL", "SOLID", "VALID", "SALAD",
                "BUYER", "SELLS", "GREEN", "CATER", "STARE", "FETCH", "LANKY", "FOILS", "DRAIN", "HEART"]

    word = random.choice(wordList)
    return word



def compareLetters(secretWord, guessLetters, wordGuess):

    for i in range(5):
        if secretWord[i] == guessLetters[i]:
            wordGuess[i] = guessLetters[i]

    if wordGuess == guessLetters:
        return True
    else:
        return False



def printLines(wordGuess, guessLetters, secretWord):

    greenLetters = []
    yellowLetters = []

    print("\n")

    # Print users guess compared to puzzle
    for i in range(5):
        print(wordGuess[i], end ="  ")

    # Green letter logic
    print("\n\nGreen Letters: ")
    for i in range(5):

        letterRepeat = False

        if wordGuess[i] != "_":
            for z in range(len(greenLetters)):
                if wordGuess[i] == greenLetters[z]:
                    letterRepeat = True
            if letterRepeat == False:
                greenLetters.append(wordGuess[i])

    # Print green letters
    for y in range(len(greenLetters)):
        print(greenLetters[y], end ="  ")



    # Yellow letter logic
    print("\nYellow Letters: ")
    for i in range(5):

        letterMatch = False

        if guessLetters[i] != secretWord[i]:

            for x in range(5):
                if guessLetters[i] == secretWord[x]:
                    letterMatch = True
                    break

            if letterMatch == True:
                letterRepeat = False
                for z in range(len(yellowLetters)):
                    if guessLetters[i] == yellowLetters[z]:
                        letterRepeat = True
                if letterRepeat == False:
                    yellowLetters.append(guessLetters[i])

    # Print yellow letters
    for y in range(len(yellowLetters)):
        print(yellowLetters[y], end ="  ")

    print("\n")


def main():
    word = getWord()
    secretWord = list(word)
    solved = False
    match = False



    print("\nWelcome to wordle! Guess 5 letter words and use the letter hints to help you make your guesses to solve the puzzle!")
    print("The green and yellow letters update after each guess.")

    for i in range(6):

        guess = input("\nGuess a 5 letter word: ").upper()
        guessLetters = list(guess)
        wordGuess = list("_____")

        while (len(guessLetters) != 5):
            print("\nMake sure your word is 5 letters!\n")
            guess = input("Guess a 5 letter word: ").upper()
            guessLetters = list(guess)

        match = compareLetters(secretWord, guessLetters, wordGuess)

        printLines(wordGuess, guessLetters, secretWord)

        if match == True:
            solved = True
            break



    # Win / lose
    if solved == True:
        print("\nYou win!")
    else:
        print("\nYou lose!")
        print("The word was", word)


main()