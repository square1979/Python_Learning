# 1.设计一个类（类比生活中，设计一张登记表）
class Student:
    name = None  # 记录学生姓名
    gender = None  # 记录学生性别
    nationality = None  # 记录学生的国籍
    native_place = None  # 记录学生的籍贯
    age = None  # 记录学生的年龄


# 2.创建一个对象（类比生活中，打印一张登记表）
stu1 = Student()

# 3. 对象属性进行赋值（类比生活中，填写表单）
stu1.name = "贺文"
stu1.gender = "男"
stu1.nationality = "中国"
stu1.native_place = "河北省"
stu1.age = 26

# 4.通过print输出记录的信息
print(stu1.name)
print(stu1.gender)
print(stu1.nationality)
print(stu1.native_place)
print(stu1.age)
# print(stu1.__dict__)
