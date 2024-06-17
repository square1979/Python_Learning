"""
    设计类，基于类创建对象，由对象做具体的工作
"""


def ring():
    import winsound
    winsound.Beep(2000, 3000)


# 设计一个闹钟类
class Clock:
    id = None
    price = None


clock1 = Clock()
clock1.id = "003032"
clock1.price = 19.99
# print(clock1.__dict__)
print(f"闹钟的编号是：{clock1.id},闹钟的价格是{clock1.price}")
ring()

clock2 = Clock()
clock2.id = "003888"
clock2.price = 149.99
# pri2t(clock1.__dict__)
print(f"闹钟的编号是：{clock2.id},闹钟的价格是{clock2.price}")
ring()
