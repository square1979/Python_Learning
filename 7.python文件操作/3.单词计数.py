"""
    通过Windows的文本编辑器软件，将下列内容，复制并保存到：word.txt 文件可以存储到任意位置
    itheima itcast python
    itheima python itcast
    beijing shanghai itheima
    shenzhen guangzhou itheima
    wuhan hangzhou itheima
    zhengzhou bigdata itheima
    通过文件读取操作，读取此文件，统计itheima单词出现的次数
"""
# first way：整合成一个长字符串，对特定字符串计数
f = open('E:/Project/word.txt', "r", encoding="utf-8")
# 读取全部内容
f1 = f.read()
# print(f"f1的结果为：{f1},其类型是：{type(f1)}")
f2 = f1.count('itheima')
print(f"【1】itheima出现的次数为：{f2}")

# Second way：先逐行读取字符串，后在每行内查找特定字符串出现次数
# 【避免一行里出现两次，出现漏记】
f = open('E:/Project/word.txt', "r", encoding="utf-8")
count = 0
for line in f:
    # print(f"每一行数据为：{line},其类型为{type(line)}")
    count += line.count('itheima')

print(f"【2】itheima出现的次数为：{count}")

# 3.Third：逐行读取为 行字符串，strip去除前后空格和换行，split根据空格分隔字符串，最后记录次数
f = open('E:/Project/word.txt', "r", encoding="utf-8")
count = 0
for line in f:
    line = line.strip()
    line = line.split(' ')
    for word in line:
        if word == 'itheima':
            count += 1

print(f"【3】itheima出现的次数为：{count}")

f.close()
