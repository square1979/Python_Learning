"""
    定义一个列表内容，内容是[1,2,3,4,5,6,7,8,9,10]
        1.遍历列表，取出列表内的偶数，并存入一个新的列表对象内
        2.使用while和for循环各操作一次
"""
# 通过while循环得出偶数列表 ———— 【循环的是自定义的参数】
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
result_1 = []
while index < len(num):
    if num[index] % 2 == 0:
        result_1.append(num[index])
    index += 1
print(f"通过while循环，从列表{num}中取出偶数，组成新列表{result_1}")

# 通过for循环得出偶数列表 ———— 【循环的是列表中的元素】
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_2 = []
for i in num:
    if i % 2 == 0:
        result_2.append(i)
print(f"通过for循环，从列表{num}中取出偶数，组成新列表{result_2}")
