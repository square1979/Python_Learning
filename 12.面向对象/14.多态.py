"""
    多种状态，完成某个行为时，使用不同的对象得到不同的状态
    以父类做定义声明，以子类做实际工作，用以获得同一行为，不同状态
    pass空实现，父类用来确定有哪些方法，具体的方法实现由子类自行决定
    抽象类：含有抽象方法的类称之为抽象类
    抽象方法：方法体是空实现【pass】称之为抽象方法
"""


class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animals: Animal):
    animals.speak()


# 演示多态，使用两个子类对象来调用函数
dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)


# 演示抽象类
class AC:
    def cool_wind(self):
        """制冷"""
        pass

    def warm_wind(self):
        """制热"""
        pass

    def swing_wind(self):
        """摆风"""
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def warm_wind(self):
        print("美的空调制热")

    def swing_wind(self):
        print("美的空调摆风")


class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def warm_wind(self):
        print("格力空调制热")

    def swing_wind(self):
        print("格力空调摆风")


def make_cool(ac: AC):
    ac.cool_wind()


midea_ac = Midea_AC()
gree_AC = GREE_AC()
make_cool(midea_ac)
make_cool(gree_AC)
