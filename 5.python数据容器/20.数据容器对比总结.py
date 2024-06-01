"""
    数据容器分类
        1.是否支持下标索引 ———— 列表[]元组() 字符串“”支持【序列类型】 集合{}，字典{}不支持
        2.是否支持重复元素 ———— 列表 元组 字符串支持【序列类型】 集合，字典不支持
        3.是否支持修改元素 ———— 列表 集合 字典支持修改 元组，字符串不支持
    基于各类数据容器的特点，它们的应用场景：
        列表:一批数据，可修改、可重复的存储场景
        元组:一批数据，不可修改、可重复的存储场景
        字符串:一串字符串的存储场景
        集合:一批数据，去重存储场景
        字典:一批数据，可用Key检索Value的存储场景
    数据容器的通用操作 - 遍历
        5类数据容器均支持for循环遍历
        列表 元组 字符串支持while循环，集合 字典不支持（无法下标索引）
    数据容器的通用统计功能 ———— len(容器)元素个数 max(容器)最大元素 min(容器)最小元素等
        其他类型不能转为字典，无法生成键值对
"""
# 定义数据容器
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
str1 = '123456789'

# 输出数据容器及其类型
print("---数据容器的长度---")
print(f"该类型为：{type(list1)},其容器为：{list1}, 其长度为：{len(list1)}")
print(f"该类型为：{type(tuple1)},其容器为：{tuple1},其长度为：{len(tuple1)}")
print(f"该类型为：{type(str1)},其容器为：{str1},其长度为：{len(str1)}")
print(f"该类型为：{type(dict1)},其容器为：{dict1},其长度为：{len(dict1)}")
print(f"该类型为：{type(set1)},其容器为：{set1},其长度为：{len(set1)}")

# max最大元素
print("---数据容器的最大元素---")
print(f"列表容器为：{list1}, 最大元素为：{max(list1)}")
print(f"元组容器为：{tuple1},最大元素为：{max(tuple1)}")
print(f"字符串容器为：{str1}, 最大元素为 {max(str1)}")
print(f"字典容器为：{dict1}, 最大元素为：{max(dict1)}")
print(f"集合容器为：{set1},  最大元素为：{max(set1)}")

# min最小元素
print("---数据容器的最小元素---")
print(f"列表容器为：{list1}, 最小元素为：{min(list1)}")
print(f"元组容器为：{tuple1},最小元素为：{min(tuple1)}")
print(f"字符串容器为：{str1}, 最小元素为 {min(str1)}")
print(f"字典容器为：{dict1}, 最小元素为：{min(dict1)}")
print(f"集合容器为：{set1},  最小元素为：{min(set1)}")

# 类型转换：容器的通用转换功能
print("------------数据容器的通用转换------------")
print("---数据容器的转换列表---")
print(f"列表转列表的结果是：{list(list1)}")
print(f"元组转列表的结果是：{list(tuple1)}")
print(f"字典转列表的结果是：{list(dict1)}")
print(f"集合转列表的结果是：{list(set1)}")
print(f"字符串转列表结果是 {list(str1)}")

print("---数据容器的转换元组---")
print(f"列表转元组的结果是：{tuple(list1)}")
print(f"元组转元组的结果是：{tuple(tuple1)}")
print(f"字典转元组的结果是：{tuple(dict1)}")
print(f"集合转元组的结果是：{tuple(set1)}")
print(f"字符转元组的结果是: {tuple(str1)}")

print("---数据容器的转换字符串---")
print(f"列表转字符串的结果是：{str(list1)}")
print(f"元组转字符串的结果是：{str(tuple1)}")
print(f"字典转字符串的结果是：{str(dict1)}")
print(f"集合转字符串的结果是：{str(set1)}")
print(f"字符转字符串的结果是: {str(str1)}")

print("---数据容器的转换集合---")
print(f"列表转集合的结果是：{set(list1)}")
print(f"元组转集合的结果是：{set(tuple1)}")
print(f"字典转集合的结果是：{set(dict1)}")
print(f"集合转集合的结果是：{set(set1)}")
print(f"字符转集合的结果是:{set(str1)}")
