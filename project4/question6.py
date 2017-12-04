from Testing import testPenData, testCarData, average, stDeviation

finalPenList = []
finalCarList = []

for i in range(0,45,5):
    tempPenList = []
    tempCarList = []
    for j in range(5):
        penResults = testPenData([i])
        carResults = testCarData([i])
        tempPenList.append(penResults[1])
        tempCarList.append(carResults[1])
    finalPenList.append(tuple([i, average(tempPenList), stDeviation(tempPenList), max(tempPenList)]))
    finalCarList.append(tuple([i, average(tempCarList), stDeviation(tempCarList), max(tempCarList)]))

print 'Pen List:', finalPenList
print 'Car List:', finalCarList


