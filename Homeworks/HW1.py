def mergeListsHere(list1, list2):

    return list1+list2


def multiplyMergedList(mergedList):
    for i in range(0, len(mergedList)):
        mergedList[i] = mergedList[i] * 2

    return mergedList


def getEvenListHere(listType):

    yourEvenList = []

    listLenght = int(input("How many elements will the {}.list be containing?".format(listType)))

    for i in range(0, listLenght):
        listElement = int(input("Enter the {0}.element of {1} List!!!".format(i+1,listType)))
        yourEvenList.append(listElement)

    return yourEvenList


def getOddListHere(listType):

    yourOddList = []
    listLenght = int(input("How many elements will the {0} list be containing?".format(listType)))

    for i in range(0, listLenght):
        listElement = int(input("Enter the {0}.element of {1} List!!!".format(i+1,listType)))
        yourOddList.append(listElement)

    return yourOddList


def isListFullOdd(myOddList):
    oddCounter = 0

    for i in range(0, len(myOddList)):
        if (myOddList[i] % 2 == 1):

            oddCounter += 1

        else:
            continue

    if (oddCounter == len(myOddList)):
        
        return True
    else:
        
        return False


def isListFullEven(myOddList):

    evenCounter = 0

    for i in range(0, len(myOddList)):
        if (myOddList[i] % 2 == 0):

            evenCounter += 1

        else:
            continue

    if (evenCounter == len(myOddList)):
        
        return True
    else:
        
        return False


def printOurNewList(latelyUpdatedList):
    for i in range(0, len(latelyUpdatedList)):
        print(
            "Order in the List: {0} Value:{1} and Type{2}".format(i, latelyUpdatedList[i], type(latelyUpdatedList[i])))


if __name__ == '__main__':


    mainList1, mainList2 = [], []

    mergedList, multipliedList = [], []

    mainList1 = getEvenListHere("Even List")
    mainList2 = getOddListHere("Odd List")

    if (isListFullOdd(mainList2) == False or isListFullEven(mainList1) == False):

        mainList1, mainList2 = [], []
        print("Please re-input the Lists!! Because you entered wrong values for the lists!!!")

        mainList1 = getEvenListHere("Even List")
        mainList2 = getOddListHere("Odd List")


    else:

        print("You entered suitable values for the lists!!!")



    mergedList = mergeListsHere(mainList1, mainList2)

    multipliedList = multiplyMergedList(mergedList)

    printOurNewList(multipliedList)
