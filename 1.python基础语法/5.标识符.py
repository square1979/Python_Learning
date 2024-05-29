# 标识符命名类型: 只允许出现英文，中文，下划线_，数字四类元素
# 不推荐使用中文；数字是不能用在开头
"""
标识符命名规范：
    见名知意：看见名字知道含义，尽量简洁
    下划线命名：多个单词组合变量名，要使用下划线做分隔
    变量中的英文字符全部小写
"""
name_worker = "张三"
print(name_worker)
_name = "李四"
print(_name)
# 大小写敏感，是能够完全区分的
Jack = "嘻嘻"
print(Jack)
jack = "不嘻嘻"
print(jack)
# 不能使用关键字
# 错误的示例：class = 1
# 错误的示例：def = 1
Class = 1
print(Class)
