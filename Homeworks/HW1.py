def mergeListsHere(list1,list2):

    return list1+list2

def multiplyMergedList(mergedList):

    for i in range(0,len(mergedList)):

        mergedList[i]=mergedList[i]*2

    return mergedList


def getListsHere(listOrder):

    yourList=[]
    listLenght=int(input("How many elements will the {0}.list be containing?".format(listOrder)))

    for i in range(0,listLenght):
        listElement = int(input("Enter the {0}.element!!!".format(i)))
        yourList.append(listElement)

    return yourList

def printOurNewList(latelyUpdatedList):

    for i in range(0,len(latelyUpdatedList)):
        print("Order in the List: {0} Value:{1} and Type{2}".format(i,latelyUpdatedList[i],type(latelyUpdatedList[i])))


if __name__ == '__main__':

    mainList1,mainList2=[], []

    mainList1=getListsHere(1)
    mainList2 = getListsHere(2)

    mergedList,multipliedList= [], []

    mergedList=mergeListsHere(mainList1,mainList2)

    multipliedList= multiplyMergedList(mergedList)

    printOurNewList(multipliedList)
