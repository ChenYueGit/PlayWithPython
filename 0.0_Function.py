def calCost(nStart, nEnd):
    nConsume = nEnd - nStart
    return 0.55*nConsume
fCost1 = calCost(1280,655)
fCost2 = calCost(3200,1777)
print(fCost1, fCost2)