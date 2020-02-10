from userFunction import updateUserScore

def score(uName, newScore):
    f = open('userScores.txt', 'r')
    for line in f:
        content = line.split(', ')
        if uName == content[0]:
            oldScore = content[1]
            print('Your score is %s:' %(oldScore))
            f.write(uName + ', ' + (newScore + oldScore) + '\n')
            f.close()

        

#theName = 'Simone'
#userName = theName
#score = '25'
#updateUserScore(userName, score)
