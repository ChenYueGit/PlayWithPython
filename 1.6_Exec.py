exec("print('test')")

scopetemp = {}
scopetemp['x'] = 30
scopetemp['y'] = 20
exec("sum = x+y", scopetemp)
print(scopetemp["sum"])