# 满足前置条件才会二次判断
"""
    if int(input("请输出你的身高：")) > 120:
    print("身高超出限制不能免费，但是VIP等级>3 可以免费进入")
    if int(input("请输入您的VIP等级：")) > 3:
        print("您的VIP等级满足条件，可以免费进入")
    else:
        print("您需要付费进入")
else:
    print("欢迎你小朋友！")
"""
age = int(input("请输入您的年龄："))
if 18 <= age < 30:
    print("您的年龄达标")
    if int(input("请输入您的入职时间：")) > 2:
        print("您可以领取礼品")
    elif int(input("您的工龄不满足，请输入您的级别：")) > 3:
        print("您可以领取礼品")
    else:
        print("您不符合领取条件")
else:
    print("您不符合领取条件")
