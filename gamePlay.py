from scienceQuestions import startScienceGame
from vocabularyQuestions import startVocabGame
from userFunction import userName, getUserScore, chooseGame

try:

# The vocab game will commence if 1 is typed
    #vg = vocabGame()
# The science game will commence if 2 is typed
    
    scienceInstructions = '''In this game, you will be given a simple
biology question.
Each correct answer gives you one mark.
No mark is deducted for wrong answers.'''
    
    vocabInstructions = '''In this game, you will be given the
definition of a word to define.
Each correct answer gives you one mark.
No mark is deducted for wrong answers.'''

# This is where the user will input their name.
    theName = input('\nPlease enter your username: ')

# This will output the usersname and score.
    print(userName(theName))

# This is where I will pull the username
# From the text file
    getUserScore(theName)

# This is where I will print the introduction
    chooseGame()

# This is where I will prompt the user to choose between
# The vocab game or science game
# I will set the userchoice to 0
    userChoice = 0
    score = 0
    sg = 'startGame'
    userChoice = input('Game Choice: ')
    while userChoice != '1' and userChoice != '2':
        print('You did not enter the correct choice. Try again.')
        userChoice = input('Game Choice: ')

    if userChoice == '1':
        print('Your choice is 1. The vocabulary game.')
        startVocabGame()   
    else:
        print('Your choice is 2. The science game.')
        startScienceGame()

        
except Exception as e:
    print('An unknown error occured. Program will exit.')
    print('Error: .', e)
        
