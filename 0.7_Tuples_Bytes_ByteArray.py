# Tuple is Read-only List
tuple1 = ("Chenxinxin","bride", True, 27)
print(type(tuple1))
print(len(tuple1))
print(tuple1.count("27"))

tuple2 = tuple((x for x in range(9)))
print(tuple2)

# bytes Read-only byte stream
buffer = b"cpcisfuckingbadass"
b2 = buffer[::-1]
print(b2)
buffer = b"\x21\x22\x32"
print(len(buffer))

#65535 = 0xffff
#65534 = oxfffe
x=65534
bufferLittle = x.to_bytes(2,"little")
bufferBig = x.to_bytes(2,"big")
print(bufferLittle, bufferBig)

y = int.from_bytes(b"\xff\xfe","little")
print(y)

#byte array
byAr= bytearray(0x00 for x in range(9))
print(byAr)
byAr[1] = 0x33
print(byAr)
for i in byAr:
    print(i)
byAr2 = bytearray(b"dsadasds")

#order
byAr2[2] = ord("b") 
print(byAr2)
#bin
print(bin(byAr2[2]))

#sequecne - list str tuple bytes bytearray
