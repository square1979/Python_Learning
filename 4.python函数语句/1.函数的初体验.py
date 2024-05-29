# 需求：统计字符串的长度，不适用len函数
str1 = "would"
str2 = "want"
str3 = "like"


# # 定义一个计数的变量
# count = 0
# for i in str1:
#     count = count + 1
# print(f"字符串{str1}的长度为：{count}")
#
# count = 0
# for j in str2:
#     count = count + 1
# print(f"字符串{str2}的长度为：{count}")
#
# count = 0
# for k in str3:
#     count = count + 1
# print(f"字符串{str3}的长度为：{count}")

# 使用函数优化这个过程 ———— 1.已组织好的 2.可重复使用 3.针对特定功能
def my_len(data):
    count1 = 0
    for i in data:
        count1 += 1
    print(f"字符串{data}的长度为{count1}")


my_len(str1)
my_len(str2)
my_len(str3)
