def main():
    word = input("Enter a word: ")
    wordArray = [1] * len(word)
    blank = []
    blankCompare = []
    error = 5
    endGame = False

    for n in range(len(word)):
        blank.append("_")
        blankCompare.append("_")
        wordArray[n] = word[n]

    while not endGame:
        teste = True
        blankCompare = blank
        palpite = input("Enter a letter: ")
        for n in range(len(word)):
            if word[n] == palpite:
                blank[n] = palpite
                teste = False
            elif n == len(word) - 1 and blankCompare == blank and teste == True:
                error = error - 1
                teste = False
        print(blankCompare, blank)
        print(f'Restam {error} chances')
        if (blank == wordArray):
            print(f'Parabéns, você acertou! A palavra era {word}')
            endGame = True
        elif (error == 0):
            print(f'Infelizmente você errou! A palavra era {word}')
            endGame = True


main()
