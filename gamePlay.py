from stemClasses import (updateScore, getUser, printInstructions,theScienceGame, vocabularyGame)

try:

# The science game will commence if 1 is typed

# The vocab game will commence if 2 is typed
    
    scienceInstructions = '''In this game, you will be given a simple
biology question.
Each correct answer gives you 1 point.'''
    
    vocabInstructions = '''In this game, you will be given the
definition of a word that you nee to define.
Each correct answer gives you 1 point.'''

    scGame = theScienceGame()
    vbGame = vocabularyGame()

# This is where the user will input their name.
    uName = input('\nPlease enter your username: ')

    score = int(getUser(uName))

    if score == -1:
        newUser = True
        score = 0
    else:
        newUser = False
        print('Welcome back %s. Your score is %d.' %(uName,score))

    userChoice = 0

    while userChoice != '-1':
        whichGame = input('(1) Science Game and (2) Vocab Game: ')
        while whichGame != '1' and whichGame != '2':
            print('That is not a valid choice.Try again')
            whichGame = input('(1) Science Game and (2) Vocab Game.')
            

        if whichGame == '1':
            printInstructions(scienceInstructions)
            score = score + scGame.scienceGame(uName)
            print('Your new overall score is %d' %(score))
        else:
            printInstructions(vocabInstructions)
            score = score + vbGame.vocabGame(uName)
            print('Your new overall score is %d.' %(score))


        userChoice = input('Press enter to continue or -1 to end: ')
        print(score)
        
        updateScore(newUser, uName, str(score))
    
except Exception as e:
    print("Error occured. Program will exit")
    print("Error: ",e)
            

        
