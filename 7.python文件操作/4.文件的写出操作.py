# 直接调用write并未真正写入文件，而是会积攒到程序的内存中
# 当调用flush的时候，才会真正写入文件，避免频繁操作硬盘，导致效率下降

f = open("E:/project/test.txt", 'w', encoding='utf-8')

# write写入
f.write('hello world')
# 将内存中积攒的内容写到硬盘文件中
# f.flush()
f.close()  # close的方法是内置了flush功能的
