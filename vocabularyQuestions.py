def startVocabGame():
    #This is where I will initialize score to 0
    score = 0
    # I have an empty dictionary 
    dict = {}
    #This is the beginning of the information to
    #be saved into the dictionary. They are stored as Keys and Values
    dict['''1.) To enclose in a circle.

A.) Inscribe
B.) Circumscribe
C.) Scribe
'''] = 'a'
    dict['''2.) To write, carve, or engrave words

A.) Inscribe
B.) Transcribe
C.) Scribe
'''] = 'b'
    dict['''3) To make full written copy of spoken material

A.) Transcribe
B.) Scribe
C.) Circumscribe
 '''] = 'c'
    dict['''4.) A small letter or number written below and to
the right of a letter or number.

A.) Proscribe
B.) Scripture
C.) Subscripture
'''] = 'd'
    dict['''5.) Sacred writings or books. Passages from sacred writings.

A.) Subscript
B.) Scripture
C.) Pescribe
'''] = 'e'
    dict['''6.) To forbid; to prohibit

A.) Proscribe
B.) Scripture
C.) Subscript
'''] = 'f'
    dict['''7.) Lacking distinctive or individual features

A.) Ascribe
B.) Nondescript
C.) Prescribe
'''] = 'g'
    dict['''8.) To identify as causing something.

A.) Proscribe
B.) Nondescript
C.) Acribe
'''] = 'h'
    dict['''9.) To give or recommend as a medical treatment or remedy.

A.) Prescribe
B.) Proscribe
C.) Acribe
'''] = 'i'
    dict['''10.) A person who copies manuscripts and documents.

A.) Inscribe
B.) Scribe
C.) Transcribe
'''] = 'j'
    # Here I will cycle through the list of questions
    for i in dict:
        print(i)
        # This is where I will prompt the user to choose a answer
        userInput = input('Please answer ')
        # The user asnwer should match the value for given key
        if userInput == dict.get(i):
            #If the user asnwers correctly then they will
            # be greeted with your answer is correct
            print('You answered correctly')
            score = score+1
            print('Your new score is: %s' %(score))
        else:
            print('You answer is incorrect')
            print('The correct answer is:', dict.get(i))
            print('Your score remains: %s' %(score))
                
    
