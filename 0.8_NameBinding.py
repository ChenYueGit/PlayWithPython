a=1
print(id(a))
a=2
print(id(a))
b=a
print(id(b))
b=a+1
print(id(b))

#is
a=3
b=3.0
print(a==b)
print(a is b) #as address is not the same

#readonly 
#int
#float
#bool
#str
#bytes
#tuple

#mendable
#list
#bytearray
l1 = ["cx","cy","crh"]
l2 = l1
l2 = ["ds"]
l1[1] = "cgq"
print(l1)
print(l2)

t1 = ("ss","sq","sd")
t2 = t1
t2 = ("sds")
print(t1,t2)