"""
    设置一个范围1-100的随机着呢概述变量
    通过while循环，配合input语句，判断输入的数字是否等于随机数
    1.无限次机会，直到猜中为止
    2.每次猜不中，会提示大了或小了
    3.猜完数字后，提示猜了几次
"""
import random

num = random.randint(1, 100)
print(num)
i = 1
guess = int(input("请输入您第1次猜想的数字"))
while num != guess:
    if guess > num:
        print("你猜大了")
    elif guess < num:
        print("你猜小了")
    i = i + 1
    guess = int(input(f"你第{i}次猜的随机数为"))

print(f"你使用{i}次机会猜中了，随机数为：{guess}")
