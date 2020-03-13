class ChenYueGirlfreind:
    __tChenYueGirlfreinds = ("LM", "GY", "JDD", "CXX")
    def getExGf(self):
        t1=self.__tChenYueGirlfreinds[0:3]
        return t1
    
class ChenYueFamaily:
    lChenYueFamilyMembers = ["Father", "Mother", "Brother", "Sister", "Nephew", "ME"]
    def __init__(self, members):
        self.lChenYueFamilyMembers.append(members)
    

cygf = ChenYueGirlfreind()
print(cygf.getExGf())
cyfam = ChenYueFamaily("CXX")
print(cyfam.lChenYueFamilyMembers)

        