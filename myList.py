myList = [2, -8, -3, 10, 5, 20, -12, 5, 11]
sortList = []

while myList:
    minNum = myList[0]
    for x in myList:
        if x < minNum:
            minNum = x
    sortList.append(minNum)
    myList.remove(minNum)


print(sortList)