#define list
l1 = ["Chen Yue", 30, "Master", "CCZU"]
l2 = ["Chen Xinxin", 27, "Bachelor", "SNU"]
#change list
l1[1] = 31
#traverse list
for i in l1:
    print(i)
#print length
print(len(l1))
#print type
print(type(l1))
#Get the last element
print(l1[-1])
#append list
l1.append("Hangzhou")
print(l1)
#insert list
l1.insert(2,"groom")
l2.insert(2,"bride")
print(l1,l2)
#pop list
l1.pop()
l2.pop(-2)
print(l1,l2)
#Remove element
l1.remove("CCZU")
print(l1,l2)
#Nest List
l3 = [l1, l2]
print(l3[0][2])
#Copy list
l4 = l3.copy()
del l4[0][1]
print(l4)
#List sorting
#l1.sort()
l4.sort(key=len)
print(l1,l4)
l4.sort(reverse = True)
print(l1,l4)
#Get new list which is sorted
l1Sorted = sorted(l1)
print(l1, l1Sorted)
#reverse the list
l1Sorted.reverse()
print(l1Sorted)
#deal with numbers
scores=[22,33,42,35,21,65]
print(max(scores))
print(len(scores))
print(min(scores))
print(sum(scores))
print(sum(scores)/len(scores))
#List quick generation
cubes = [x**3 for x in range(1,10)]
print(cubes)
print(sum(cubes))
#Create matrix
matrix = [[0]*8]*10
for i in range(0,len(matrix)):
    print(matrix[i])
#Add list
l5 = l1 + l2
print(l5)
#count
print(l5.count("Chen Xinxin"))
#clear
print(l5.clear())
print(l5)
#extend
l5.extend(["test1", "test2"])
print(l5)
#index
i=l5.index('test1')
print(i)
#get address
print(id(l5))
#slice
numbers = [x for x in range(10)]
print(numbers[3:9])
# str1 = "test1"
# str2 = str1[0:1]
# print(str2)
print(numbers[3:])
print(numbers[0:9])
print(numbers[-6:-1])
print(numbers[1:9:2])
print(numbers[-1:1:-2])
#get a new reversed list
numberReversed=numbers[::-1]
print(numberReversed)