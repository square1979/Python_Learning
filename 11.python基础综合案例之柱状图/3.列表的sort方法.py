"""
    列表的sort方法：
    列表.sort（key = 根据排序依据的函数， reverse = True/False）
    参数KEY 传入一个函数，将该列表的每一个元素都传入函数中，返回排序的依据
    参数reverse 是否反转排序结果，True表示降序 False表示升序
"""
my_list = [["a", 33], ["b", 55], ["c", 11]]

# 定义一个函数返回列表的第二个元素
# def choose_sort(element):
#     return element[1]
#
#
# # 以列表的第二个元素进行排序
# my_list.sort(key=choose_sort, reverse=True)
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)
