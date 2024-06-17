"""
    运行结果 5g关闭，使用4g网络
            正在通话中
    意义：可以定义不直接对用户开放的属性和行为
"""


#  设计一个手机类，内部包含：
class Phone:
    # 1.私有成员变量：_is_5g_enable,类型为bool, True表示开启5g,False表示关闭5g
    __is_5g_enable = True

    #  2.私有成员方法：_check_5g() 会判断私有成员_is_5g_enable的值
    #         若为True 打印输出 5g开启
    #         若为False 打印输出 5g关闭,使用4g网络
    @staticmethod
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭,使用4g网络")

    #     3.公开成员方法：call_by_5g(),调用它会执行
    #         调用私有成员方法：_check_5g(),判断5g网络状态
    #         打印输出：正在通话中
    def call_by_5g(self):
        self.__check_5g(self)
        print("正在通话中")


phone = Phone()
phone.call_by_5g()
