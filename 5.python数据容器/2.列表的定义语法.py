"""
    通过中括号 [] 作为标识
    列表中每个元素之间用逗号隔开，每一个数据称为一个元素，元素类型不受限制
    定义空列表：
        变量名称 = []
        变量名称 = list()
"""
name_list1 = ['once', 666, 'a', True]
name_list2 = [['one', 'two', 'three', 'four'], ['five', 'six', 'seven', 'eight']]
print(f"{name_list1}, \n {name_list2}")
print(f"{type(name_list1)}\n{type(name_list2)}")
