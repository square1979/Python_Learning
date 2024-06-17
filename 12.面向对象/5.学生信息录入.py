"""
    设计一个类，记录学生的：姓名 年龄 地址 三类信息
    要求：
        1.通过for循环，配合input语句，并使用构造方法，完成学生信息的键盘录入
        2.输入完成后，使用print语句，完成信息的输出
"""


# 1.构造方法
class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


students = []
# 2.for循环
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in nums:
    print(f"当前录入第{num}位学生信息，总共需要录入10位学生信息")
    # stu = Student
    # stu.name = input(print("请输入学生姓名："))
    # stu.age = input(print("请输入学生年龄："))
    # stu.address = input(print("请输入学生地址："))
    # 现象：可以赋值并输出，但是输出结果会多“None”
    # 原因：在调用 input() 时使用了 print() 作为参数，而 print() 函数会返回 None，
    # 因此在执行 input(print("请输入学生姓名：")) 时会先执行 print("请输入学生姓名：")，
    # 然后将其返回值 None 传给 input() 函数，导致在终端中出现 None。
    # 此外，应该在每次循环中创建一个新的 Student 对象并存储到一个列表中，便于后续输出所有学生的信息
    student_name = input("请输入学生姓名：")
    student_age = input("请输入学生年龄：")
    student_address = input("请输入学生地址：")
    student = Student(student_name, student_age, student_address)
    students.append(student)

    print(f"学生{num}信息录入完成，"
          f"信息为：【学生姓名：{student.name},年龄：{student.age},地址：{student.address}】")
