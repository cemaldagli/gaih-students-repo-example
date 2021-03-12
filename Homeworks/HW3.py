midtermVar, checkBool, projectVar, finalVar,result=[],[],[],[],[]


studentDict ={ 1: "False", 2 : "False", 3: "False", 4: "False", 5: "False"}

def getMidtermGrade(listType,studID):

        midGrade = int(input("Enter the {0} Grade for Student {1}: ".format(listType,studID)))


        return midGrade


def getProjectGrade(listType,studID):

    projectGrade = int(input("Enter the {0} Grade for Student {1}: ".format(listType,studID)))

    return projectGrade


def getFinalGrade(listType,studID):

        finalGrade = int(input("Enter the {0} Grade for Student {1}: ".format(listType,studID)))

        return finalGrade


def calculateAverage(mid,project,final):

    return (0.3*mid)+(0.3*project)+(0.4*final)



def isPassed(average):

    if average >=50:

        return True

    else:
        return False


def printValues():

    listExtentions = ["", "st", "nd", "rd", "th", "th"]

    for i in range(0, 5):
        tempMidtermVar = getMidtermGrade("Midterm",i+1)
        midtermVar.append(tempMidtermVar)

        tempProjectVar = getProjectGrade("Project",i+1)
        projectVar.append(tempProjectVar)

        tempFinalVar = getFinalGrade("Final",i+1)
        finalVar.append(tempFinalVar)

        tempResult = calculateAverage(tempMidtermVar, tempProjectVar, tempFinalVar)
        result.append(tempResult)

        tempcheckBool = isPassed(result[i])
        checkBool.append(tempcheckBool)


    for i in range(0,5):

        checkLambdaFunction = lambda checkBool: "Passed" if checkBool else "Failed"

        studentDict[i]=checkLambdaFunction(checkBool[i])


    for i in range(0,5):

        print("---------------------------- {0}.{1} Student --> {2} Average:{3}----------------------------".format(i + 1,
                                                                                                   listExtentions[
                                                                                                       i + 1],
                                                                                                    studentDict[i],
                                                                                                                 result[i]))



if __name__ == '__main__':

    printValues()


