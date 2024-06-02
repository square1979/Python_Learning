"""
    内存中存放的数据关机后回消失，需要使用硬盘，光盘等设备，长久保存数据
    为了便于数据的管理和检索，引入了“文件”的概念
    文件操作包括【打开，关闭，读写】

    1.open() 打开函数
        语法：open(name,mode,encoding)
            name 是打开的目标文件名的字符串（可以包含文件所在的具体路径）
            mode 设置打开文件的模式（访问模式）：只读、写入、追加等
            encoding 编码格式（推荐使用UTF-8）
        示例代码：
            f = open('python.txt','r',encoding='utf-8')
            【encoding 的顺序不是第三位，所以不能用位置参数，用关键字参数直接指定】
            文件写入使用“w"模式 原有内容会被删除，如果文件不存在，创建新文件
            文件用于追加“a"模式 新内容回写入已有内容之后，文件不存在，则创建新文件写入
            文件只读打开“r"模式 文件的指针回会放在文件的开头。这是默认模式
"""

# 打开文件


# 读取文件

# 1.read() 方法：文件对象.read(num)，从文件中读取的数据的长度（单位是字节）;
#   若没有num则读取全部数据
# 注意：连续调用两次read语句，第二次会从第一次结束位置开始读取
f = open("E:/Project/测试.txt", "r", encoding="utf-8")
print(f"读取十个字节的结果：{f.read(10)},{type(f.read(10))}")
print(f"读取全部字节的结果：{f.read()}")

# 2.readlines() 方法：按照行的方式把整个文件中的内容进行一次习惯读取
#   返回一个列表，每一行的数据为一个元素 【指针读完了，所以输出为空】
f = open("E:/Project/测试.txt", "r", encoding="utf-8")
lines = f.readlines()
print(f"lines对象的类型：{type(lines)}\t内容是：{lines}")

# 3.readline() 方法：一次读取一行
f = open("E:/Project/测试.txt", "r", encoding="utf-8")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"第一行数据是：{line1}")
print(f"第二行数据是：{line2}")
print(f"第三行数据是：{line3}")

# 4.for循环读取文件行
for line in f:
    print(f"每一行数据为：{line}")

# 文件关闭,停止文件占用
# time.sleep(500000)
f.close()
# time.sleep(500000)

# with open 语法操作文件,执行完自动将文件关闭
with open("E:/Project/测试.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"每一行的数据是：{line}")

# time.sleep(500000)
