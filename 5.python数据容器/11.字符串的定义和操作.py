# 字符的容器，数据长度任意的容器，只能存储字符串，不可以修改
# 字符串的索引：从前向后，下标从零开始；从后向前，下标从-1开始
# 本节函数：查找下标【index】 替换元素【replace】 分割字符串【split】
#         去除前后字符串【strip】 记录出现次数【count】统计长度【len】
# 定义一个字符串
my = "abandon"
value = my[2]
value2 = my[-1]
print(f"下标为0的元素为：{value}\n"  f"下标为-1的元素为：{value2}")
# 字符串不支持修改
# my[2] = 'q'
# print(my)

# 查找特定元素的下标值
a = my.index("d")
print(f"在my字符串中查找d的下标为：{a}")

# 字符串的替换 语法：字符串.replace（字符串1， 字符串2）
# 不是修改字符串本身而是得到新的字符串
my_new = my.replace("a", "邢")
print(f"将字符串:{my} 的a替换为邢后的字符串为:{my_new}")

# 字符串的分隔
# 语法：字符串.split（分隔符字符串）
# 功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
# 注意：字符串本身不变，而是得到了一个新的列表对象
my_str = "123451234512345"
b = my_str.split("5")
print(f"将my_str:{my_str}\t通过数字5切分多个字符串结果为：{b}")

# 字符串的常用操作
# 语法：字符串.strip（）
# 功能：去除前后空格
# 语法：字符串.strip（字符串）
# 功能：去除前后指定字符串
my_char = "  i am not you   "
my_char1 = my_char.strip()  # 不传入参数去除首尾空格
print(f"字符串：{my_char}去除空格后的字符串为：{my_char1}")

my_str = "123i am not you 321"
my_str1 = my_str.strip("123")  # 分成子串 “1” “2” “3”
print(f"字符串：{my_str}去除123后的字符串为：{my_str1}")

# 统计字符串中特定元素出现的次数 count
my_str = "i am not you father"
c = my_str.count("t")
print(f"字符串：{my_str}里‘t’出现的次数为: {c}")

# 统计字符串的长度 len()
my_num = len(my_str)
print(f"字符串：{my_str}的长度为：{my_num}")

# 字符串的遍历之while循环
my_str = "黑马程序员"
index = 0
while index < len(my_str):
    print(my_str[index])
    index += 1

# 字符串的遍历之for循环
my_str = "呼叫大公鸡"
for char in my_str:
    print(char)
