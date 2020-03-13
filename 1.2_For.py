# for      interable object
# s = ""
# for x in "abcd":
#     s = s + x + "-"
#     print(x)
#     print(s)
    
# sum = 0
# for x in range(1, 100, 2):
#     sum += x
# print(sum)

# sMessage = ""
# while sMessage != "q":
#     sMessage = input("press q to quit..").strip().lower()
# print("quited")

# Continue
for x in range(1,10):
    if x==1:
        continue
    print(x)
    
matrix = [[ x + y for x in range(3)] for y in range(4)]
for x in range(len(matrix)):
    print(matrix[x],"\n")

for c in range(3):
    for r in range(4):
        matrix[r][c] *=2

for x in range(len(matrix)):
    print(matrix[x]) 
    


