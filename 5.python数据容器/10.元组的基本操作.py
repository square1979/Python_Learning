"""
    定义一个元组，内容是：('周杰伦',11,['football','music'])
    记录的是一个学生的信息（姓名、年龄。爱好）
    要求：通过元组的功能方法对其进行：
        1.查询其年龄所在位置的下标位置
        2.查询学生的姓名
        3.删除学生爱好中的football
        4.增加爱好：coding到list内
"""
# 定义一个元组
info = ('周杰伦', 11, ['football', 'music'])
# 查询其年龄所在位置的下标位置
index = 0
while index < len(info):
    if type(info[index]) is int:
        print(f"其年龄所在位置的下标位置:{index}")
    index = index + 1

# 查询学生的姓名
for j in info:
    if type(j) is str:
        print(f"学生的姓名为：{j}")

# 删除学生爱好中的football
info[2][0] = ''
print(f"删除学生爱好中的football后结果为：{info}")

# 增加爱好：coding到list内
info[2][0] = 'coding'
print(f"增加爱好：coding到list内后结果为：{info}")
