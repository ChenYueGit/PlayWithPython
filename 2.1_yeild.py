def generateFibonacci(endNumber):
    a, b, count = 0, 1, 0
    while True:
        if count>endNumber:
            return
        else:
            yield a
            a, b = b, a+b
            count += 1
        
f = generateFibonacci(10)
print(f)

a = [x for x in f]
print(a)