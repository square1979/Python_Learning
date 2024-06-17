"""
    复写：子类继承父类的成员属性和成员方法后，如果对其“不满意”，那么可以进行复写
        即：在子类中重新定义同名的属性或方法即可
    用父类的同名成员：需要被复写的父类的成员，需要用特殊方法调用调
        1.通过父类名去调用:父类名.成员变量【父类名.成员方法（self）】
        2.使用super() 调用父类成员：使用成员变量:super().成员变量【super().成员方法】
"""


class Phone:
    IMEI = None
    producer = "google"

    def call_by_5g(self):
        print("使用父类的5g网络进行通话")


# 定义子类，复写父类成员
class Phone2023(Phone):
    producer = "marks"

    def call_by_5g(self):
        print("子类的5g网络通话")
        # 方式1
        print(f"父类的厂商是:{Phone.producer}")
        Phone.call_by_5g(self)
        # 方法2
        # print(f"父类的厂商是:{super().producer}")
        # super().call_by_5g()

        print(f"子类的厂商是:{phone.producer}")
        print("关闭CPU单核模式，确保性能")


phone = Phone2023()
phone.call_by_5g()
print(phone.producer)
