"""
    列表可修改元素；元组一旦定义完成不可修改
    元组使用小括号（）定义，可以存储多个数据使用逗号隔开数据，数据可以是不同的数据类型
    数据是有序存储（下标索引）；允许重复元素出现，支持for循环
"""
# 定义元组 如果元组内只有一个元素，要在其后面加逗号
t1 = (1, 'a', ['b', 'c'], ['d', 'e'])
t2 = ()
t3 = tuple()
t4 = (5,)
print(f"t1元组是{t1},其类型是{type(t1)}")
print(f"t2元组是{t2},其类型是{type(t2)}")
print(f"t3元组是{t3},其类型是{type(t3)}")
print(f"t4元组是{t4},其类型是{type(t4)}")

# 元组的嵌套
t5 = ((1, 2), (3, 4))
print(f"t5元组是{t5},其类型是{type(t5)}")

# 元组通过下标索引取出内容
print(f"从嵌套元组中取出的数据是：t5[1][1]")

# 元组的相关操作:
# 查找元素————index()
one = ('船只', 'python', 666, 'also')
index = one.index('python')
print(f"在one元组中查找python，其下标为：{index}")

#  统计元素出现次数————count()
two = (666, 'python', 666, 'also', 'only', 'also')
count = two.count(666)
print(f"在two元组中查找666，其次数为：{count}")

# 统计元组内的元素个数————len()
three = (512, 'those', 512, 'also', 'onto', 'anto', (5, 2,))
length = len(three)
print(f"在three元组中统计元素个数为：{length}")

# 元组的遍历———— while实现
index = 0
while index < length:
    print(f"通过while循环输出元组的元素有：{three[index]}")
    index += 1

# 元组的遍历———— for实现
print("------------------------------------")
for i in three:
    print(f"通过for循环输出元组的元素有：{i}")

# 元组不可修改，但是元组内部的列表可以修改
t6 = (1, 2, 3, 4, ['a', 'b', 'c'])
print(f"t6的内容是：{t6}")
t6[4][1] = 'what'
t6[4][2] = 'are'
print(f"t6的内容是：{t6}")
