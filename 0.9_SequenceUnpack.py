numbers = 1,2,3
print(type(numbers),numbers)
x,y,z = numbers
print(x,y,z)
x,y,z = ["x",32,True]
print(x,y,y)

#*rest
d,*rest = numbers
print(d) 

a,*rest,b = "Chen Yue"
print(a,b)
