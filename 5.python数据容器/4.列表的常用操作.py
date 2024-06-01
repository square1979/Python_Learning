"""
    列表的特点：
        1.可以容纳多个元素（上限为2**63-1）
        2.可以容纳不同类型的元素
        3.数据是有序存储的，有下标
        4.允许重复数据存在
        5.可以修改（增加或删除元素等）
"""
my_list = ['a', 'b', 'c', 'd', 'e']
print(f"初始列表的元素为：{my_list}")
# 1.查询功能：查找指定元素在列表的下标，如果 找不到/不存在 则报错valueError
# 语法：列表.index(元素)
index = my_list.index('d')
print(f"通过index方式查找'd'元素在列表中的的下标为：{index}")

# 修改功能：修改指定元素在列表的元素值
# 语法：列表[下标] = 值
my_list[2] = 'Q'
print(f"通过赋值方式修改my_list[2]为“Q”\n此时列表的元素为：{my_list}")

# 2.插入功能：在指定位置，插入指定元素
# 语法：列表.insert(下标，元素)
my_list.insert(2, 'T')
print(f"通过insert方式插入my_list[2] = 'T'\n此时列表的元素为：{my_list}")

# 3.列表中进行元素的追加
# 语法：列表.append(元素)
my_list.append('f')
print(f"通过append方式追加元素'f' \n此时列表的元素为：{my_list}")

# 4.列表中进行元素的追加一批元素
# 语法：列表.extend(其他数据容器)，将其他数据容器的内容取出，依次追加到列表尾部
my_word = ['hello', 'world']
my_list.extend(my_word)
print(f"通过extend方式追加了['hello', 'world']\n此时列表的元素为：{my_list}")

# 5.列表中只能进行元素的删除
# 语法：del列表[下标]
del my_list[-1]
print(f"通过del方式删除下标[-1]\n此时列表的元素为：{my_list}")

# 6.列表中不仅能删除元素还能把删除的元素作为返回值去得到
# 语法：列表.pop(下标)
print(f"通过pop方式取出下标[-1]：{my_list.pop(-1)}\n此时列表的元素为：{my_list}")

# 7.列表删除某元素在列表中的第一个匹配项
# 语法：列表.remove（元素）
my_list.remove('Q')
print(f"通过remove用法移除元素'Q'\n此时列表的元素为：{my_list}")

# 8.清空列表
# 语法：列表.clear（）
my_list.clear()
print(f"通过clear用法清空元素 \n此时列表的元素为：{my_list}")

# 9.统计列表中某个元素的数量
# 语法：列表.count（元素）
my_char = ['a', 'b', 'c', 'd', 'e', 'a', 'a']
print(f"通过count用法统计元素'a' \n此时列表的‘a'元素数量为：{my_char.count('a')}")

# 10.统计列表中所有元素的数量
# 语法：len(列表)
print(f"通过len用法统计所有元素 \n此时列表的元素数量为：{len(my_char)}")
