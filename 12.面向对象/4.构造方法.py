"""
    通过传参的方式对属性赋值 ———— 通过构造方法
    python类可以使用 __init__() 称之为构造方法
    创建类对象的时候自动执行
    创建类对象的时候，将传入参数自动传递给__init__方法使用

    注意:1.前面两个下划线，后面两个下划线 中间init
        2. 构造方法也是成员方法，不要忘记在参数列表中提供：self
        3.在构造方法内定义成员变量，需要使用self关键字
            def __init__(self, name, age, tel)
                self.name = name
                self.age = age
                self.tel = tel
        变量是定义在构造方法内部，如果要成为成员变量，需要用self来表示
"""


# 构造方法的名称： __init__

class Student:
    # name = None
    # age = None
    # tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("student类创建了一个类对象")


# 先输入的数据，再调用类函数
stu = Student("周杰伦", 31, "13212100000")
print(stu.name)
print(stu.age)
print(stu.tel)
