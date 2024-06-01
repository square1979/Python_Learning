"""
    add 添加元素    remove移除元素  pop随机取出元素   clear 清空元素
    different得到差集   different_update在集合1里删除集合2中的重复元素
    union 得到两集合的并集  len得到集合元素的数量

    列表可修改，支持重复元素且有序；元组，字符串不可修改，支持重复元素且有序
    列表使用[] 元组使用（） 字符串使用 “ ” 集合使用{}
    Tips:1.count() 函数是列表(list)的一个方法,用于统计列表中某个元素出现的次数。
    但是集合是一种无序且不重复的数据结构,它的特点是每个元素都是唯一的。
        2.数据是无序存储，不允许重复元素，不能使用下标
        3.可以用for循环输出元素，不能用while
"""
# 集合的定义
my_set = {"stars", "soar", "eat", "rain", "stars", "soar", "eat", "rain"}
my_set_empty = set()
print(f"my_set的内容是：{my_set}，其类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty}，其类型是：{type(my_set_empty)}")

# 集合的常用操作【无顺序，不能使用下标索引】
# 添加新元素 add
my_set = {"python", "java", "ruby", "javascript", "javascript"}
my_set.add("黑马程序员")
print(my_set)
my_set.add("java")  # 去重
print(my_set)

# 移除元素 remove
my_set.remove("java")
print(my_set)

# 随机取出元素 集合.pop
element = my_set.pop()
print(f"集合取出元素为：{element},取出元素后结果为：{my_set}")

# 集合被清空 clear
my_set.clear()
print(my_set)

# 取两个集合的差集
set1 = {1, 2, 3, 4, 5, 9}
set2 = {1, 2, 3, 4, 5, 6}
set3 = set1.difference(set2)
print(f"差集为set3:{set3}")
print(f"取出差集后的set1:{set1}")
print(f"取出差集后的set2:{set2}")

# 消除2个集合里面相同的元素，在集合1里面消除和集合2的元素
set1 = {1, 2, 3}
set2 = {1, 4, 5}
set1.difference_update(set2)
print(f"消除差集后的set1:{set1}")
print(f"消除差集后的set2:{set2}")

# 两个集合合并 集合1.union（集合2），得到新结果但是集合1，集合2不变 ———— 不会修改原来集合
set1 = {1, 2, 3}
set2 = {1, 4, 5}
set5 = set1.union(set2)
print(f"合并的结果set5:{set5}")
print(f"合并后的set1:{set1}")
print(f"合并后的set2:{set2}")

# 统计集合的元素数量len
num = len(set1)
print(f"集合set1的长度为：{num}")

# 集合的遍历不能使用while循环可以使用for循环
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for i in set1:
    print(i)
