"""
    有字符串："万过薪月，员序程马黑来，nohtyp学"
    请使用学过的任何方法，得到“黑马程序员”
    可用方式：
        倒序字符串，切片后取出或切片取出，然后倒序
        split分隔，replace替换“来”为空，倒序字符串
"""
# 倒序字符串，切片后取出
str1 = "万过薪月，员序程马黑来，nohtyp学"
str2 = str1[::-1]
str3 = str2[9:14:1]
print(str3)

# 切片取出，然后倒序
str_1 = "万过薪月，员序程马黑来，nohtyp学"
str_2 = str_1[9:4:-1]
print(str_2)

# split分隔，replace替换“来”为空，倒序字符串
str_1 = "万过薪月，员序程马黑来，nohtyp学"
str_2 = str_1.split("，")  # ['万过薪月', '员序程马黑来', 'nohtyp学']
str_3 = str_2[1].replace("来", "")  # 员序程马黑
str_4 = str_3[::-1]
print(str_4)
