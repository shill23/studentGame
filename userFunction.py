#User will enter their username
def userName(uName):
    return 'Welcome %s' %(uName)
#Based on the users game selection certain
#instructions will print
def printInstructions(instructions):
    print(instructions)
#This is where the user will choose the game
    #They want to play
def userChoice(anSwer):
    sg = scienceGame
    vg = vocabGame
# This is the function used to get the user score
# I will pull this information from a text file
# That contains usernames and user scores
def getUserScore(userName):
    f = open('userScores.txt', 'r')
    for i in f:
        contentofFile = i.split(', ')
        if userName == contentofFile[0]:
            print('''User %s is found
Your score is %s
''' %(userName, contentofFile[1]))


# This is the function that I will use to choose
# The user game based off a selection of 1 or 2
def chooseGame():
    introduction = str('''\nPlease choose between the Vocabulary Game
and the Science Game. Type 1 for the Vocab Game
and type 2 for the Science Game.''')
    print(introduction)

def updateUserScore(userName, score):
    from os import remove, rename
    temp = open('userScores.tmp', 'w')
    input = open('userScores.txt', 'r')
    for line in input:
        content = line.split(', ')
        if content[0] == userName:
            oldScore = content[1]
            print(oldScore + score)
            temp.write(userName + ', ' + score + oldScore)
        else:
            temp.write(line)
    input.close()
    temp.close()

    remove('userScores.txt')
    rename('userScores.tmp', 'userScores.txt')
    print('Hello from function')
    
    
           
        
        
            



    
         
                

                

        
        
