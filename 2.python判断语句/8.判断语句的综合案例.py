import random

num = random.randint(1, 10)
print(num)
a = int(input("猜第一次数字："))
if a != num:
    print("你猜错了")
    if a > num:
        print("猜测数大于随机数")  # 第一次猜大了
    else:
        print("猜测数小于随机数")  # 第一次猜小了
    b = int(input("猜第二次数字："))
    if b != num:
        print("你猜错了")
        if b > num:
            print("猜测数大于随机数")  # 第二次猜大了
        else:
            print("猜测数小于随机数")  # 第二次猜小了
        c = int(input("猜第二次数字："))
        if c != num:
            print("你猜错了")
            if c > num:
                print("猜测数大于随机数")  # 第三次猜大了
            else:
                print("猜测数小于随机数")  # 第三次猜小了
        else:
            print("你猜对了")
    else:
        print("你猜对了")
else:
    print("你猜对了")
