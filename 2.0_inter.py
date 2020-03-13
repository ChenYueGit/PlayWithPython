gf = ["LM", "GY", "JDD", "CXX"]
it_gf = iter(gf)
print(next(it_gf))
print("test")
print(next(it_gf))
# for x in it_gf:
#     print(x)
while True:
    try:
        print(next(it_gf))
    except StopIteration:
        pass    
    