"""
    面向对象的编程是基于模板类去创建实体，使用对象完成功能开发
    定义私有成员的方式非常简单，只需要：
        私有成员变量：变量名以__开头（2个下划线）
        私有成员方法：方法名以__开头（2个下划线）
"""


# 定义一个类，内含私有成员变量和私有成员方法
class phone:
    __current_voltage = 1

    @staticmethod  # 普通函数转换为静态方法。
    def __keep_single_core():
        print("CPU以单核运行")

    def call_by_5G(self):
        if self.__current_voltage >= 1:
            print("满足要求")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，单核进行省电")


phone = phone()
phone.call_by_5G()
# 私有的类对象不能直接使用，私有变量只能在内部使用
# phone.__keep_single_core()
# print(phone.__keep_single_core)
