    
def printInstructions(instructions):
    instructions = str
    print(instructions)
                
def getUser(uName):
    try:    
        f = open('userName.txt','r')
        for line in f:
            contentofFile = line.split(',')
            if uName == contentofFile[0]:
                score = int(contentofFile[1])
                welcomeMessage ='Welcome back %s.\nYour score is %d.' %(uName,score)
                print(welcomeMessage)
                f.close()
                return score
        f.close()
        return '-1'
    except IOError:
        print('File not found. An new file will be created.')
        f = open('userName.txt','w')
        f.close()
        return '-1'


# Testing function          
# theUser = getUser('Bob')

def updateScore(newUser,uName,score):
    from os import remove, rename
    if newUser == True:
        f = open('userName.txt','a')
        f.write('\n'+ uName + ',' + score)
        f.close()
    else:
        t = open('userName.tmp','w')
        f = open('userName.txt','r')
        for line in f:
            contentofFile = line.split(',')
            if contentofFile[0] == uName:
                t.write(uName + ',' + score + '\n')
            else:
                t.write(line)
        f.close()
        t.close()

        remove('userName.txt')
        rename('userName.tmp','userName.txt')

# Testing function
# upScore = updateScore(False,'Simone','2000')
class theScienceGame:
    def scienceGame(uName,score):
        import xlrd
        score = 0
        #print('Welcome %s. Your score is %d.'%(uName,score))
        loc = ("/Users/simonehill/Desktop/PYTHON FILES/studentGame/quizQuestions.xlsx")
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        for i in range(sheet.nrows):
            print('\n'+sheet.cell_value(i,0))
            userChoice = input('Please enter your answer:')
            while True:
                try:
                    if userChoice == sheet.cell_value(i,1):
                        print('You answered correctly')
                        score = score +1
                        print('Your current game score is %s'%(score))
                        break
                    else:
                        print('Wrong answer.\nThe correct answer is:',sheet.cell_value(i,1))
                        print('You current game score is still %s.' %(score))
                        break
                except:
                    print('Not a valid answer')
        return score
# Testing the function           
# theGame = scienceGame('Simone',0)
class vocabularyGame:
    def vocabGame(uName, score):
        import xlrd
        score = 0
        print('Welcome %s. Your score is %d.'%(uName,score))
        loc = ("/Users/simonehill/Desktop/PYTHON FILES/studentGame/quizQuestions.xlsx")
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(1)
        for i in range(sheet.nrows):
            print('\n'+sheet.cell_value(i,0))
            userChoice = input('Please enter your answer:')
            while True:
                try:
                    if userChoice == sheet.cell_value(i,1):
                        print('You answered correctly')
                        score = score +1
                        print('Your current game score is %s'%(score))
                        break
                    else:
                        print('Wrong answer.\nThe correct answer is:',sheet.cell_value(i,1))
                        print('You current game score is still %s.' %(score))
                        break
                except:
                    print('You did not enter a valid answer.')
        return score
    #def retainScore(score):
        
# Testing the function
# vocabGame = vocabGame('Simone',0)

    

