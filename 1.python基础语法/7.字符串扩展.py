# 字符串的定义形式，三引号用变量接收是字符串，不用变量接收就是注释
name1 = 'look'
name2 = "looking"
name3 = """
looking for
"""
print(name1, name2, name3)
print(type(name1), type(name2), type(name3))
# 字符串包含双引号
name4 = '"john"'  # 双引号作为字符串内容显示
print(name4, type(name4))
# 字符串包含单引号
name5 = "'jack'"
print(name5, type(name5))  # 单引号作为字符串内容显示
# 使用转义字符 \
name6 = "\"jack"
print(name6, type(name6))  # "jack 使用转义符进行引号的嵌套
name7 = '\'jack\''
print(name7, type(name7))  # 'jack'
