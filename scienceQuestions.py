
def startScienceGame():
    
#The initial score will be 0
    score = 0
#The dictionary will be empty 
    dict = {}
#This is the beginning of the questions passed to dictionary
#They will be save as Key and Value inside the dictionary
    dict[''''______ are comprised of extra-chromosomal DNA and are
present in many species of bacteria and archaea.
a.) Pilus
b.) Fiber
c.) Chitin
d.) Plasmids
'''] = 'a'
    dict['''Which of the following extremophiles needs a
high sugar concentration for optimal growth?
a.) Acidophiles
b.) Halophiles
c.) Osmophiles
d.) Thermophiles
'''] = 'b'
    dict['''The Rickettsia that causes typhus and
Rocky Mountain spotted fever belongs to
the ______ class of the phylum Proteobacteria.
a.) Myxobacteria
b.) Gammaproteobacteria
c.) Alphaproteobacteria
d.) Betaproteobacteria
'''] = 'c'
    dict['''______is a nitrogen-fixing endosymbiont
associated with the roots of legumes.
a.) Rhizobium
b.) Rickettsia
c.) Spirillum minus
d.) Nitrosomonas
'''] = 'd'
    dict['''What is the species of beta proteobacteria
that causes rat-bite fever?
a.) Spirillum minus
b.) Rhizobium
c.) Rickettsia
d.) Nitrosomonas
'''] = 'e'
    dict['''What disease often results in a characteristic
bullseye rash?
a.) Justinian plague
b.) Lyme disease
c.) Athenian plague
d.) Black Death
'''] = 'f'
    dict['''What reduced the population of Europe by
50 percent between 541 and 750?
a.) Brucellosis
b.) Typhoid
c.) Justinian plague
d.) Athenian plague
'''] = 'g'
    dict['''What causes food poisoning?
a.) Treponema pallidum
b.) Salmonella
c.) Bacillus anthracis
d.) Vibrio cholera
'''] = 'h'
    dict['''What illness results in 200,000 deaths and has about
16 to 33 million cases reported annually?
a.) Typhoid
b.) Justinian plague
c.) Athenian plague
d.) Black Death
'''] = 'i'
    dict['''______ reduced the world’s population from an estimated
450 million to about 350 to 375 million.
a.) Black Death
b.) Athenian plague
c.) Justinian plague
d.) Typhoid
'''] = 'j'
#I will cycle through the list of questions
    for i in dict:
    #Here the user inputs a letter
        print(i)
        userInput = input('Please answer ')
    #If the user input is equal to the value of the key -->
        if userInput == dict.get(i):
        #The score will increase
            score = score + 1
        #Print out your answer is correct
            print('your answer is correct')
        #Print out the new score
            print('Your new score is:', score)
        else:
        #Else print your answer is wrong
        #Score will not be printed because -->
        #It does not update to new score
                print('wrong answer')
        print('The correct answer is:' ,dict.get(i))
        f = open('userScores.txt', 'r')
    for line in f:
        print(line)

        




