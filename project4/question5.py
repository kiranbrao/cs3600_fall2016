from Testing import testPenData, testCarData, average, stDeviation

penList = []
carList = []

for i in range(5):
    penResults = testPenData()
    penList.append(penResults[1])
    carResults = testCarData()
    carList.append(carResults[1])

print 'Pen', penList
print 'Car', carList
penAverage = average(penList)
penStDev = stDeviation(penList)
penMax = max(penList)

carAverage = average(carList)
carStDev = stDeviation(carList)
carMax = max(carList)

print 'Pen:', penAverage, penStDev, penMax
print 'Car:', carAverage, carStDev, carMax

