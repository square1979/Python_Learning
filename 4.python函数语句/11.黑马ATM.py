"""
    定义一个全局变量：money，用来记录银行卡余额（默认5000000）
    定义一个全局变量：name，用来记录客户的姓名（启动程序时输入）
    定义如下函数：
        1.查询余额函数
        2.存款函数
        3.取款函数
        4.主菜单函数
    要求：
        1.程序启动后要输入客户的姓名
        2.查询余额，存取款后会返回主菜单
        3.存取款后，都应显示一下当前余额
        4.客户选择退出或者输入错误，程序会退出，否则程序持续运行
"""


def cun(jia, name1):
    global money
    money += jia
    print("----------存款----------")
    print(f"{name1},您好，您存款{jia}元成功")
    print(f"存款后的金额为：{money}元")
    return money


def qu(jian, name1):
    global money
    money -= jian
    print("----------取款----------")
    print(f"{name1},您好，您存款{jian}元成功")
    print(f"取款后的金额为：{money}元")
    return money


def menu(char):
    global money
    if char == "1":
        jia = int(input("请输入您要存入的金额(元):"))
        cun(jia, name)
    elif char == "2":
        jian = int(input("请输入您要取款的金额(元):"))
        qu(jian, name)
    elif char == "3":
        print("----------查询余额----------")
        print(f"您当前的余额为：{money}元")


name = input("请输入您的名字：")
print("----------主菜单----------")
print(f"{name}，您好！欢迎您来到黑马ATM")
money = 5000000
choice = ""
while True:
    print("请选择您要选择的业务项目:")
    print("\t1.存款\n\t2.取款\n\t3.查询余额\n\t4.退出项目")
    choice = input("请输入服务项目的数字:")
    if choice == "1" or choice == "2" or choice == "3":
        menu(choice)
    else:
        break
