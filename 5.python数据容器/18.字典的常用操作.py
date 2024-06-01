# 字典的定义
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(f"初始的字典结果为：{dict1}")

# 新增元素：字典[key] = value 字典被修改，增加了新元素 此时需要满足 key不存在
dict1['f'] = 6
print(f"增加'f'= 5的字典结果为：{dict1}")

# 更新元素：字典[key] = value 字典被修改，元素被更新  此时需要满足 key已存在
dict1['a'] = 6
print(f"修改'a'= 6的字典结果为：{dict1}")

# 删除元素：字典.pop(key) 获得指定key的value，同时字典被修改，指定key数据被删除
dict1.pop('d')
print(f"删除'd'= 4的字典结果为：{dict1}")

# 清空元素：字典.clear
dict1.clear()
print(f"清空字典结果为：{dict1}")

# 获取全部key：字典.keys() 得到字典里的全部key值
dict1 = {'赵': 1, '钱': 2, '孙': 3, '李': 4, '周': 5}
print(f"字典里的key值有：{dict1.keys()},其格式为：{type(dict1.keys())}")

# 遍历字典
# 1.通过获取全部被的key来完成遍历
for key in dict1.keys():
    print(f"字典的key是：{key} value值为：{dict1[key]}")

# 2.直接对字典进行for循环，每一次循环都是直接得到key
for key in dict1:
    print(f"for循环遍历字典: {key} value值为：{dict1[key]}")

# 统计字典内key的数量
print(f"字典内key的数量为：{len(dict1)}")
