"""
open(file, mode='r',buffering=-1,encoding=none,errors=none,newline=none,closefd=true,opener=None)
file:：必须，文件路径（相对或绝对路径）
mode：可选
buffering：设置缓冲
encoding：一般用 utf8
errors：报错级别
newline：区分换行符
closefd：传入的file参数类型
opener
more information could be found in the following link
https://www.runoob.com/python3/python3-file-flush.html
"""
path1 = "/Volumes/CY's SSD/1_Work/To Do List/Internal Sharing/C211EV_VCU_CANEV.S19"
f_read = open(path1,mode="r")
path2 = "/Users/chenyue/Documents/Cache/test.s19"
f_write = open(path2,"w")
i = 0
l = []
for line in f_read:
    f_write.write(str(i)+"\t"+line)
    l.append(line)
    i+=1
f_read.close()
f_write.close()
print(l[-1])