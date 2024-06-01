# 容器通用排序功能 sorted
# 定义数据容器
list1 = [3, 2, 1, 4, 5, 6, 7, 8, 9]
tuple1 = (4, 3, 2, 1, 5, 6, 7, 8, 9)
dict1 = {'b': 1, 'd': 2, 'a': 3, 'c': 4}
set1 = {9, 8, 7, 4, 5, 6, 1, 2, 3}
str1 = '123456789'

print("---数据容器的元素正向排序生成列表类型---")
print(f"列表容器为：{list1}, 元素排序为：{sorted(list1)} ，其类型为{type(sorted(list1))} ")
print(f"元组容器为：{tuple1},元素排序为：{sorted(tuple1)}，其类型为{type(sorted(tuple1))} ")
print(f"字符串容器为：{str1}, 元素排序为 {sorted(str1)}  ，其类型为{type(sorted(str1))} ")
print(f"字典容器为：{dict1}, 元素排序为：{sorted(dict1)} ，其类型为{type(sorted(dict1))} ")
print(f"集合容器为：{set1},  元素排序为：{sorted(set1)}  ，其类型为{type(sorted(set1))}")

print("---数据容器的元素反向排序生成列表类型---")
print(f"列表容器为：{list1}, 元素排序为：{sorted(list1, reverse=True)} ")
print(f"元组容器为：{tuple1},元素排序为：{sorted(tuple1, reverse=True)}")
print(f"字符串容器为：{str1}, 元素排序为 {sorted(str1, reverse=True)}  ")
print(f"字典容器为：{dict1}, 元素排序为：{sorted(dict1, reverse=True)} ")
print(f"集合容器为：{set1},  元素排序为：{sorted(set1, reverse=True)}  ")
