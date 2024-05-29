import random

num = random.randint(1, 10)
print(num)
guess = int(input("猜第一次数字："))
if guess == num:
    print("猜中了")
else:
    if guess > num:
        print("猜大了")
    else:
        print("猜小了")
    guess = int(input("猜第二次数字："))
    if guess == num:
        print("猜中了")
    else:
        if guess > num:
            print("猜大了")
        else:
            print("猜小了")
        guess = int(input("猜第三次数字："))
        if guess == num:
            print("猜中了")
        else:
            if guess > num:
                print("猜大了")
            else:
                print("猜小了")
