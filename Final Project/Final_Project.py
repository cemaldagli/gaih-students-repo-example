questionNumber,userPoint, correctAnswerNumber=0,0,0
checkResultBoolean=False
questionsList=["In which year of First World War Germany declared war on Russia and France?\n (a) 1914 (b) 1915 (c) "
               "1916 (d) 1917",
               "ICAO stands for : \n (a) International Civil Aviation Organization (b) Indian Corporation of "
               "Agriculture Organization (c) Institute of Company of Accounts Organization (d)None",
               "In which season do we need more fat? \n (a) None (b) Spring (c) Winter (d) Summer",
               "In a normal human body, the total number of red blood cells is \n (a) 30 trillion (b) 15 trillion (c) "
               "25 trillion (d) 27 trillion",
               "How many players are there on each side in the game of Basketball? \n(a) 4 (b) 5 (c) "
               "6 (d) 7 ",
               "If force is expressed in Newton and the distance in metre, then the work done is expressed in \n(a) Joule "
               "(b) KgW (c) "
               "KgWm (d) Watt ",
               "How many teeth does a normal adult dog have?\n (a) 42 (b) 44 (c) "
               "32 (d) 34",
               "How many red blood cells does the bone marrow produce every second?\n (a) 3 million (b) 5 million (c) "
               "4 million (d) 2 million",
               "How many times has Brazil won the World Cup Football Championship?\n (a) 3 (b) 5 (c) "
               "4 (d) 6",
               "If speed of rotation of the earth increases, weight of the body\n (a) decreases (b) increases (c) "
               "remains unchanged (d) may decrease or increase",]

answersList=["a","a","c","a",
             "b","a","a","d","b","a"]



listExtentions = ["", "st", "nd", "rd", "th", "th", "th", "th", "th", "th", "th"]





def printQuestion(questionNo):

    print("\n{0}.{1} Question: ".format(questionNo + 1, listExtentions[questionNo + 1]))
    print("{0}".format(questionsList[questionNo]))



def findQuestion(questionNumber):

    printQuestion(questionNumber)


def checkTheAnswer(answerNumber):

    userAnswer=input("Please Enter the Answer!!!")



    if userAnswer == answersList[i]:



        return True

    else:

        return False








if __name__ == '__main__':

    for i in range(0,10):

        findQuestion(i)

        checkResultBoolean= checkTheAnswer(i)

        if checkResultBoolean==True:
            correctAnswerNumber += 1

            userPoint += 10
            print("Your Answer is correct. Your Point is: {0} Your Total Correct Questions: {1}".format(userPoint, correctAnswerNumber))
            continue

        else:

            print("Your answer is NOT correct!Your Point is: {0} Your Total Correct Questions: {1}".format(userPoint, correctAnswerNumber))
            print("Keep Answering!!!")


    if correctAnswerNumber >= 5:

        print("\nYour are successful!!!")


    else:

        print("\nYou are NOT successfull!!!")

